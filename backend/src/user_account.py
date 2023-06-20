from router import *

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