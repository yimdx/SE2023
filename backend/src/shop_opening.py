import datetime
from router import *

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
    if not checkIID(info['identificationID']):
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
    transaction = f"SELECT * FROM openningRequestForm WHERE submitStatus='Success'"
    cursor.execute(transaction)
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
    return 'Success'

@netshop.route("/admin/checkOpenningRequest/sendBack", methods=['POST', 'GET'])
def openingRequestSendBack():
    # Change submitStatus to sendBack
    # Front end should provide userName
    userName = request.json.get('userName')
    mutex.acquire()
    cursor.execute("UPDATE openningRequestForm SET submitStatus='sendBack' WHERE userName=%s", userName)
    conn.commit()
    mutex.release()
    return 'Success'

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