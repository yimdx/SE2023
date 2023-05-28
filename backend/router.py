from flask import Flask, jsonify, redirect, render_template, request, session, url_for
import pymysql
from pymysql import cursors
import datetime
# from flask_jwt_extended import JWTManager, jwt_required
from flask_caching import Cache
from utils import checkIID
from utils.data_structures import account, adminAccounts
from utils.cross_requests import deleteGoodRequest
from threading import Lock

netshop = Flask(__name__)
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', 
                       passwd='', charset='utf8', db='db',cursorclass=cursors.DictCursor)
mutex = Lock()
#use the database db containing openningRequestForm and clientInfo
cursor = conn.cursor()
'''
netshop.config['JWT_SECRET_KEY'] = 'your-secret-key'
netshop.config['JWT_ALGORITHM'] = 'HS256'
netshop.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=1)
'''

# jwt = JWTManager(netshop)
cache = Cache(config={"CACHE_TYPE": "simple"})
cache.init_app(netshop)

@netshop.route("/test")
def testAccessibility():
    return "Hello from backend!"

################################################# Registration #################################################
@netshop.route("/register", methods=['POST', 'GET'])
def userAccountRegistration():
    username = request.json.get('username')
    password = request.json.get('password')
    userType = request.json.get('userType')
    idNumber = request.json.get('idNumber')
    phoneNumber = request.json.get('phoneNumber')
    email = request.json.get('email')
    if account.insert(username, password, userType, idNumber, phoneNumber, email):
        return ("OK", 200)
    else:
        print('userAccountRegistration failure')
        return ("RegistrationFailed", 201)

################################################# Login #################################################

def generalLogin() -> str:
    username = request.json.get('username')
    password = request.json.get('password')
    # print(username, password, str(account.auth(username, password)))
    if account.auth(username, password):
        return "Success", 200
    else: 
        return "AuthenticationFailed", 201

@netshop.route("/admin/login", methods=['POST', 'GET'])
def adminLogin():
    return generalLogin()

@netshop.route("/buyer/login", methods=['POST', 'GET'])
def buyerLogin():
    return generalLogin()

@netshop.route("/seller/login", methods=['POST', 'GET'])
def sellerLogin():
    return generalLogin()

################################################# Account #################################################

def general_personalInfo() -> dict:
    username = request.json.get('username')
    res = account.query(username)
    return {
        'username': res['username'],
        'phoneNumber': res['phoneNumber'],
        'emailPrefix': res['email'].split('@')[0],
        'emailSuffix': res['email'].split('@')[1],
        'idCode': res['idNumber'],
        'password': res['password']
    }

def general_personalInfo_modify():
    newUserName = request.json.get('username')
    password = request.json.get('password')
    phoneNumber = request.json.get('phoneNumber')
    idNumber = request.json.get('idCode')
    email = request.json.get('email')
    oldUserName = account.queryOnSecondaryKey('idNumber', idNumber)
    res = account.change(oldUserName, newUserName, password, phoneNumber, email)
    status = (200 if res == 'Success' else 201)
    return res, status

def general_personalAccount():
    username = request.json.get('username')
    res = account.query(username)
    return {
        'account': username,
        'balance': res['balance']
    }

def getShopBalance():
    shopName = request.json.get('account')
    mutex.acquire()
    query = f'SELECT balance from shopList where shopName={shopName}'
    cursor.execute(query)
    mutex.release()
    return shopName, cursor.fetchall()[0]

@netshop.route("/buyer/personalInfo", methods=['POST', 'GET'])
def buyer_personalInfo():
    return general_personalInfo()

@netshop.route("/seller/personalInfo", methods=['POST', 'GET'])
def seller_personalInfo():
    return general_personalInfo()

@netshop.route("/buyer/personalInfo/modify", methods=['POST', 'GET'])
def buyer_personalInfo_modify():
    return general_personalInfo_modify()

@netshop.route("/seller/personalInfo/modify", methods=['POST', 'GET'])
def seller_personalInfo_modify():
    return general_personalInfo_modify()

@netshop.route("/buyer/personalAccount", methods=['POST', 'GET'])
def buyer_personalAccount():
    return general_personalAccount()

@netshop.route("/seller/personalAccount", methods=['POST', 'GET'])
def seller_personalAccount():
    return general_personalAccount()

@netshop.route("/seller/personalAccount/recharge", methods=['POST', 'GET'])
def seller_personalAccount_recharge():
    username = request.json.get('account')
    value = request.json.get('recharge')
    account.recharge(username, value)
    return 'Success', 200

@netshop.route("/seller/shopAccount", methods=['POST', 'GET'])
def seller_shopAccount():
    shopName, balance = getShopBalance()
    return {
        'account': shopName,
        'balance': balance
    }

@netshop.route("/seller/shopAccount/recharge", methods=['POST', 'GET'])
def seller_shopAccount_recharge():
    shopName, balance = getShopBalance()
    recharge = request.json.get('recharge')
    mutex.acquire()
    query = f'UPDATE shopList SET balance={balance+recharge} where shopName={shopName}'
    cursor.execute(query)
    conn.commit()
    mutex.release()
    return 'Success', 200

@netshop.route("/admin/profitAccount", methods=['POST', 'GET'])
def admin_profitAccount():
    return adminAccounts.profitAccountShow()

@netshop.route("/admin/medianAccount", methods=['POST', 'GET'])
def admin_medianAccount():
    return adminAccounts.medianAccountShow()

################################################# Delete Good #################################################

@netshop.route("/merchant/store/delete", methods=['POST', 'GET'])
def merchant_store_delete():
    userName = request.json.get('userName')
    shopName = request.json.get('shopName')
    name = request.json.get('name')
    discription = request.json.get('discription')
    picture = request.json.get('picture')
    price = request.json.get('price')
    stock = request.json.get('stock')
    deleteGoodRequest.insert(userName, shopName, name, discription, picture, price, stock)
    return 'Success', 200

@netshop.route("/admin/checkDeletingRequest", methods=['POST', 'GET'])
def admin_checkDeletingRequest():
    return jsonify(deleteGoodRequest.getAll())

@netshop.route("/admin/checkDeletingRequest/Passed", methods=['POST', 'GET'])
def admin_checkDeletingRequest_Passed():
    userName = request.json.get('userName')
    shopName = request.json.get('shopName')
    name = request.json.get('name')
    deleteGoodRequest.agree(userName, shopName, name)
    transaction = f''
    cursor.execute(transaction)
    conn.commit()
    return 'Success', 200

################################################# ShopOpening #################################################

def checkInfo(info): 
    # return 1/0 for correct/incorrect
    # a dictionary "clientInfo" is supposed to be in MySQL
    mutex.acquire()
    checkRepeatedShopName = 'select * from openningRequestForm where shopName=%s'
    cursor.execute(checkRepeatedShopName, info['shopName'])
    repeatedShopName = cursor.fetchall()
    mutex.release()
    if repeatedShopName:
        return 0
    if len(info['shopName']) > 12 or not info['shopName']:
        return 0
    if not checkIID.checkIID(info['identificationID']):
        return 0
    mutex.acquire()
    checkRepeatedIID = 'select * from openningRequestForm where identificationID=%s'
    cursor.execute(checkRepeatedIID, info['identificationID'])
    RepeatedIID = cursor.fetchall()
    mutex.release()
    if RepeatedIID:
        return 0
    if len(info['shopIntro']) > 128 or not info['shopIntro']:
        return 0
    if len(info['address']) > 32 or not info['address']:
        return 0 
    if info['initialFund'] < 1000 or not info['initialFund']:
        return 0 
    return 1
@netshop.route("/admin/index/stores", methods=['POST', 'GET'])
def showShops():
    mutex.acquire()
    cursor.execute("SELECT * FROM shopList")
    result = cursor.fetchall()
    mutex.release()
    return jsonify(result=result), 200


@netshop.route("/admin/index/mystores", methods=['POST', 'GET'])
def showMyShops():
    userName = request.json.get('userName')
    mutex.acquire()
    transaction = f"SELECT * FROM shopList WHERE userName='{userName}'"
    cursor.execute(transaction)
    result = cursor.fetchall()
    mutex.release()
    return jsonify(result=result), 200

@netshop.route("/admin/checkOpenningRequest", methods=['POST', 'GET'])
def checkOpeningRequest():
    # Update the data in openning request form 
    # and return the page of examination and approve
    mutex.acquire()
    cursor.execute("SELECT * FROM openningRequestForm WHERE submitStatus='%s'"% 'Success')
    result = cursor.fetchall()
    mutex.release()
    return jsonify(result=result), 200

@netshop.route("/admin/checkOpenningRequest/Passed", methods=['POST', 'GET'])
def openingRequestPassed():
    # Add data to the table shopList, and change submitStatus to Passed
    # Front end should provide all data to add a new row to the table shopList 
    userName = request.json.get('userName')
    shopName = request.json.get('shopName')
    goodsType = request.json.get('goodsType')
    identificationID = request.json.get('identificationID')
    shopIntro = request.json.get('shopIntro')
    address = request.json.get('address')
    initialFund = request.json.get('initialFund')
    startTime = request.json.get('startTime')
    mutex.acquire()
    insertStr = 'INSERT INTO shopList \
        (userName, shopName, goodsType, identificationID, shopIntro, address, initialFund, startTime) \
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
    values = (userName, shopName, goodsType, identificationID, shopIntro, address, initialFund, startTime)
    cursor.execute(insertStr, values)
    conn.commit()
    cursor.execute("UPDATE openningRequestForm SET submitStatus='Passed' WHERE userName=%s", userName)
    conn.commit()
    mutex.release()

@netshop.route("/admin/checkOpenningRequest/sendBack", methods=['POST', 'GET'])
def openingRequestSendBack():
    # Change submitStatus to sendBack
    # Front end should provide userName
    userName = request.json.get('userName')
    mutex.acquire()
    cursor.execute("UPDATE openningRequestForm SET submitStatus='sendBack' WHERE userName=%s", userName)
    conn.commit()
    mutex.release()

@netshop.route("/store/request/commit", methods=['POST', 'GET', 'PUT'])
def openningRequestCommited():
    info = {}
    userName = request.json.get('userName')
    #userName = "seller"
    shopName = request.json.get('shopName')
    goodsType = request.json.get('goodsType')
    identificationID = request.json.get('identificationID')
    shopIntro = request.json.get('shopIntro')
    address = request.json.get('address')
    initialFund = int(request.json.get('initialFund'))
    startTime = datetime.datetime.now().strftime('%Y-%m-%d')
    
    info['userName'] = userName
    info['shopName'] = shopName
    info['goodsType'] = goodsType
    info['identificationID'] = identificationID
    info['shopIntro'] = shopIntro
    info['address'] = address
    info['initialFund'] = initialFund
    info['startTime'] = startTime
    print(f"##########userName={userName}##########")
    if checkInfo(info) == 0: 
        error = "用户信息不符合规范，请按说明修改后再提交。"
        return jsonify(error = error),444
        #error detected
    
    insertStr = 'insert into openningRequestForm(userName, shopName, goodsType, identificationID, shopIntro, address, initialFund, startTime, submitStatus) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    values = (userName, info['shopName'], info['goodsType'], info['identificationID'], info['shopIntro'], info['address'], info['initialFund'], info['startTime'], 'Success')
    mutex.acquire()
    cursor.execute(insertStr, values)
    conn.commit()
    mutex.release()
    message = "开店请求已受理。"
    return jsonify(message = message),200

################################################# Seller Commodity #################################################
# def getGoodsList(): #get its name
#     userName = request.json.get('userName')
#     formName = 'goodsListOf' + userName
#     return formName

@netshop.route("/merchant/goodsList", methods=['GET', 'POST'])
def goodsList():
    #"userName" needs to be cached after login
    formName = "goodsList"
    merchantName = request.json.get('merchantName')
    mutex.acquire()
    transaction = f"SELECT * FROM {formName} where merchantName='{merchantName}'"
    #print(f"###########{transaction}###########")
    cursor.execute(transaction)
    result = cursor.fetchall()
    mutex.release()
    return jsonify(result=result),200
    #front end should update the filename here 
    
def checkCommodityInfo(info):
    if info["name"] == None:
        return 0
    if len(info["name"]) > 64:
        return 0
    if info["discription"] == None:
        return 0
    if len(info["discription"]) > 128:
        return 0
    if info["picture"] == None:
        return 0
    if info["price"] <= 0:
        return 0
    if info["price"] == None:
        return 0
    if info["stock"] == None:
        return 0
    if info["stock"] <= 0:
        return 0
    return 1

@netshop.route("/merchant/goodsList/add/commit", methods=['GET', 'POST'])
def upShelfRequestCommited():
    #we adfter end will cache userName and shopName
    userName = request.json.get('userName')
    shopName = request.json.get('shopName')
    name = request.json.get('name')  #this "name" is the name of goods
    discription = request.json.get('discription')
    picture = request.json.get('picture')
    price = request.json.get('price')
    stock = request.json.get('stock')
    info = {
    "name":name, "discription":discription, 
    "picture":picture, "price":price, "stock":stock 
    }
    if checkCommodityInfo(info) == 0:
        error = "信息不符合规范，请按说明修改后再提交。"
        return jsonify(error = error),444

    #userName, shopName, name, discription, picture, price, stock, submitStatus
    ss = 'Submitted'
    insertStr = f"insert into upShelfRequest(userName, shopName, \
        name, discription, picture, price, stock, submitStatus) \
        values ('{userName}', '{shopName}', '{info['name']}', '{info['discription']}', \
        '{info['picture']}', '{info['price']}', '{info['stock']}', '{ss}')"
    mutex.acquire()
    print(f"upShelfRequestCommited: #########{insertStr}###############")
    cursor.execute(insertStr)
    conn.commit()
    mutex.release()
    message = "新增商品请求已受理。"
    return jsonify(message = message), 200

@netshop.route("/merchant/goodsList/alter", methods=['GET', 'POST'])
def MCIRequest():
    #receive userName and name for selection
    #and post former commodity information
    name = request.json.get('name')
    formName = "goodsList"
    mutex.acquire()
    cursor.execute('SELECT name, discription, picture, price, stock FROM {0} where name={1}'.format(formName, name))
    result = cursor.fetchall()
    mutex.release()
    #here I just post the necessary information 
    return jsonify(result=result), 200

@netshop.route("/merchant/goodsList/alter/commit", methods=['GET', 'POST'])
def MCIRequestCommited():
    userName = request.json.get('userName')
    shopName = request.json.get('shopName')
    name = request.json.get('name')
    discription = request.json.get('discription')
    picture = request.json.get('picture')
    price = request.json.get('price')
    stock = request.json.get('stock')
    info = {
    "name":name, "discription":discription, 
    "picture":picture, "price":price, "stock":stock 
    }
    print("###########################")
    print(info)
    if checkCommodityInfo(info) == 0:
        error = "信息不符合规范，请按说明修改后再提交。"
        return jsonify(error = error),444

    #userName, shopName, name, discription, picture, price, stock, submitStatus
    ss = 'Submitted'
    insertStr = 'insert into MCIRequest(userName, shopName, name, discription, picture, price, stock, submitStatus) values (%s, %s, %s, %s, %s, %s, %s, %s)'
    values = (userName, shopName, info['name'], info['discription'], info['picture'], info['price'], info['stock'], ss)
    mutex.acquire()
    cursor.execute(insertStr, values)
    conn.commit()
    mutex.release()
    message = "修改商品信息请求已受理。"
    return jsonify(message = message), 200

@netshop.route("/merchant/goodsList/downShelf", methods=['GET', 'POST'])
def downShelf():
    name = request.json.get('name')
    formName = "goodsList"
    mutex.acquire()
    cursor.execute("update {0} set shelf={1} where name='{2}'".format(formName, 'down', name))
    conn.commit()
    mutex.release()

@netshop.route("/merchant/goodsList/delete", methods=['GET', 'POST'])
def deleteGoods():
    name = request.json.get('name')
    formName = "goodsList"
    mutex.acquire()
    transaction = "delete from {0} where name='{1}'".format(formName, name)
    cursor.execute(transaction)
    conn.commit()
    mutex.release()

@netshop.route("/merchant/goodsList/upShelfRequestList", methods=['GET', 'POST'])
def upShelfRequestList():
    userName = request.json.get("userName")
    mutex.acquire()
    transaction = f"SELECT * FROM {'upShelfRequest'} where userName='{userName}'"
    cursor.execute(transaction)
    result = cursor.fetchall()
    # print(f"################ {transaction}")
    # print(result)
    mutex.release()
    return jsonify(result=result), 200

@netshop.route("/merchant/goodsList/upShelfRequestList/delete", methods=['GET', 'POST'])
def deleteUpShelfRequest():
    userName = request.json.get("userName")
    name = request.json.get('name')
    mutex.acquire()
    transaction = f"delete from upShelfRequest where userName='{userName}' and name='{name}'"
    cursor.execute(transaction)
    conn.commit()
    mutex.release()
    return 'Success'

@netshop.route("/merchant/goodsList/upShelfRequestList/alter", methods=['GET', 'POST'])
def alterUpShelfRequest():
    userName = request.json.get("userName")
    name = request.json.get('name')
    mutex.acquire()
    cursor.execute('SELECT name, discription, picture, price, stock FROM {0} where userName={2} and name={1}'.format("upShelfRequest", userName, name))
    result = cursor.fetchall()
    mutex.release()
    #here I just post the necessary information 
    return jsonify(result=result), 200
#"alterUpShelfRequest"is a little different from "addAGoods", so we need to programme them respectively

@netshop.route("/merchant/goodsList/upShelfRequestList/alter/commit", methods=['GET', 'POST'])
def upShelfRequestAlternationCommited():
    # we adfter end will cache userName and shopName
    userName = request.json.get('userName')
    name = request.json.get('name')  #this "name" is the name of goods
    discription = request.json.get('discription')
    picture = request.json.get('picture')
    price = request.json.get('price')
    stock = request.json.get('stock')
    info = {
    "name":name, "discription":discription, 
    "picture":picture, "price":price, "stock":stock 
    }
    if checkCommodityInfo(info) == 0:
        error = "信息不符合规范，请按说明修改后再提交。"
        return jsonify(error = error), 444

    ss = 'Submitted'
    insertStr = 'update upShelfRequest set name=%s, discription=%s, picture=%s, price=%s, stock=%s, submitStatus=%s where userName=%s'
    values = (info['name'], info['discription'], info['picture'], info['price'], info['stock'], ss, userName)
    mutex.acquire()
    cursor.execute(insertStr, values)
    conn.commit()
    message = "修改新增商品申请表成功。"
    mutex.release()
    return jsonify(message = message), 200

@netshop.route("/merchant/goodsList/MCIRequestList", methods=['GET', 'POST'])
def MCIRequestList():
    userName = request.json.get("userName")
    mutex.acquire()
    transaction = f"SELECT * FROM {'MCIRequest'} where userName='{userName}'"
    cursor.execute(transaction)
    result = cursor.fetchall()
    # print(f"################ {transaction}")
    # print(result)
    mutex.release()
    return jsonify(result=result), 200

@netshop.route("/merchant/goodsList/MCIRequestList/delete", methods=['GET', 'POST'])
def deleteMCIRequest():
    userName = request.json.get("userName")
    name = request.json.get('name')
    mutex.acquire()
    transaction = f"delete from MCIRequest where userName='{userName}' and name='{name}'"
    cursor.execute(transaction)
    conn.commit()
    mutex.release()
    return 'Success'

@netshop.route("/merchant/goodsList/MCIRequestList/alter", methods=['GET', 'POST'])
def alterMCIRequest():
    userName = request.json.get("userName")
    name = request.json.get('name')
    mutex.acquire()
    cursor.execute('SELECT name, discription, picture, price, stock FROM {0} where userName={2} and name={1}'.format("MCIRequest", userName, name))
    result = cursor.fetchall()
    mutex.release()
    #here I just post the necessary information 
    return jsonify(result=result), 200

@netshop.route("/merchant/goodsList/MCIRequestList/alter/commit", methods=['GET', 'POST'])
def MCIRequestCommited_MCIRequestList():
    userName = request.json.get('userName')
    newName = request.json.get('newName')
    discription = request.json.get('discription')
    picture = request.json.get('picture')
    price = request.json.get('price')
    stock = request.json.get('stock')
    info = {
    "name":newName, "discription":discription, 
    "picture":picture, "price":price, "stock":stock 
    }
    if checkCommodityInfo(info) == 0:
        error = "信息不符合规范，请按说明修改后再提交。"
        return jsonify(error = error), 444

    #userName, shopName, name, discription, picture, price, stock, submitStatus
    ss = 'Submitted'
    insertStr = 'update MCIRequest set name=%s, discription=%s, picture=%s, price=%s, stock=%s, submitStatus=%s) where userName=%s'
    values = (info['name'], info['discription'], info['picture'], info['price'], info['stock'], ss, userName)
    mutex.acquire()
    cursor.execute(insertStr, values)
    conn.commit()
    mutex.release()
    message = "对修改商品信息申请表的修改成功。"
    return jsonify(message = message), 200

################################################# Admin Commodity #################################################

def updateSubmitStatus(formName, submitStatus):
    userName = request.json.get('userName')
    name = request.json.get('name')
    # cursor = conn.cursor()
    mutex.acquire()
    insertStr = f"update {formName} set submitStatus='{submitStatus}' where \
        userName='{userName}' and name='{name}'"
    cursor.execute(insertStr)
    conn.commit()
    mutex.release()

def selectListwithSubmitStatus(formName, submitStatus):
    # cursor = conn.cursor()
    transaction = "SELECT * FROM %s where submitStatus='%s'" % (formName, submitStatus)
    mutex.acquire()
    cursor.execute(transaction)
    res = cursor.fetchall()
    mutex.release()
    return res

@netshop.route("/admin/checkUpShelfRequest", methods=['GET', 'POST'])
def checkUpShelfRequest():
    result = selectListwithSubmitStatus("upShelfRequest", "Submitted")
    print(result)
    return jsonify(result=result), 200

@netshop.route("/admin/checkUpShelfRequest/Passed", methods=['GET', 'POST'])
def upShelfRequestPassed_Passed():
    updateSubmitStatus("upShelfRequest", "Passed")
    return "Success"

@netshop.route("/admin/checkUpShelfRequest/sendBack", methods=['GET', 'POST'])
def upShelfRequestPassed_sendBack():
    updateSubmitStatus("upShelfRequest", "sendBack")
    return "Success"

@netshop.route("/admin/checkMCIRequest", methods=['GET', 'POST'])
def checkUpShelfRequest_MCIRequestSubmitted():
    result = selectListwithSubmitStatus("MCIRequest", "Submitted")
    return jsonify(result=result), 200

@netshop.route("/admin/checkMCIRequest/Passed", methods=['GET', 'POST'])
def upShelfRequestPassed_MCIRequestPassed():
    updateSubmitStatus("MCIRequest", "Passed")
    return "Success"

@netshop.route("/admin/checkMCIRequest/sendBack", methods=['GET', 'POST'])
def upShelfRequestPassed_MCIRequestsendBack():
    updateSubmitStatus("MCIRequest", "sendBack")
    return "Success"

################################################# Cart #################################################

def askForGoodsStatus(goodsName):
    formName = "goodsList"
    mutex.acquire()
    transaction = f"select shelf from {formName} where name='{goodsName}'"
    cursor.execute(transaction)
    result = cursor.fetchall()
    mutex.release()
    if not result[0]:
        return None # This goods didn't exist.
    return result[0]['shelf'] 

# def getCart():
#     # get its name
#     userName = request.json.get('userName')
#     formName = 'cartOf' + userName
#     return formName

@netshop.route("/user/cart", methods=['GET', 'POST'])
def cart():
    cartName = 'cart'
    buyerName = request.json.get("buyerName")
    mutex.acquire()
    transaction = f"select * from {cartName} where buyerName='{buyerName}' "
    cursor.execute(transaction)
    preResult = cursor.fetchall()
    mutex.release()
    for tpl in preResult:
        goodsStatus = askForGoodsStatus(tpl['goodsName'])
        insertStr = f"update {cartName} set shelf='{goodsStatus}' \
    where goodsName='{tpl['goodsName']}'"
        mutex.acquire()
        cursor.execute(insertStr)
        conn.commit()
        mutex.release()
    mutex.acquire()
    cursor.execute(transaction)
    result = cursor.fetchall()
    mutex.release()
    return jsonify(result=result), 200

@netshop.route("/addingToCart", methods=['GET', 'POST'])
def addingToCart():
    buyerName = request.json.get("buyerName")
    merchantName = request.json.get("merchantName")
    goodsName = request.json.get("goodsName")
    picture = request.json.get("picture")
    unitPrice = request.json.get("unitPrice")
    quantity = request.json.get("quantity")
    insertStr = f"insert into cart(buyerName,merchantName, goodsName, picture, \
    unitPrice, quantity) values({buyerName},{merchantName}, {goodsName}, \
    {picture}, {unitPrice}, {quantity})"
    mutex.acquire()
    cursor.execute(insertStr)
    conn.commit()
    mutex.release()

@netshop.route("/user/cart/delete", methods=['GET', 'POST'])
def deleteFromCart():
    buyerName = request.json.get("buyerName")
    goodsName = request.json.get("goodsName")
    cartName = 'cart'
    mutex.acquire()
    insertStr = f"delete from {cartName} where \
    buyerName='{buyerName}' and goodsName='{goodsName}'"
    cursor.execute(insertStr)
    conn.commit()
    mutex.release()

if __name__ == "__main__":
    try:
        netshop.run(host="127.0.0.1", port=3000, debug=True)
    finally:
        #shut down MySQL
        cursor.close()
        conn.close()
