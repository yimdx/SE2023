from router import *

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
def upShelfRequestPassed():
    updateSubmitStatus("upShelfRequest", "Passed")
    merchantName = request.json.get('userName')
    name = request.json.get('name')
    transaction_ask = f"SELECT userName, name, discription, \
        picture, price, stock FROM upShelfRequest WHERE userName = '{merchantName}' AND name = '{name}'"
    mutex.acquire()
    cursor.execute(transaction_ask)
    result = cursor.fetchall()
    #print(result[0]['discription'],' ',result[0]['picture'],' ',result[0]['price'],' ',result[0]['stock'])
    transaction_insert = f"insert into goodsList(merchantName,name,discription,picture,price,stock,shelf)\
        values('{merchantName}','{name}','{result[0]['discription']}','{result[0]['picture']}',\
            {result[0]['price']},{result[0]['stock']},'up')"
    cursor.execute(transaction_insert)
    conn.commit()
    mutex.release()
    return "Success"

@netshop.route("/admin/checkUpShelfRequest/sendBack", methods=['GET', 'POST'])
def upShelfRequestSendBack():
    updateSubmitStatus("upShelfRequest", "sendBack")
    return "Success"

@netshop.route("/admin/checkMCIRequest", methods=['GET', 'POST'])
def checkMCIRequest():
    result = selectListwithSubmitStatus("MCIRequest", "Submitted")
    return jsonify(result=result), 200

@netshop.route("/admin/checkMCIRequest/Passed", methods=['GET', 'POST'])
def MCIRequestPassed():
    updateSubmitStatus("MCIRequest", "Passed")
    merchantName = request.json.get('userName')
    name = request.json.get('name')
    transaction_ask = f"SELECT userName, name, discription, \
        picture, price, stock FROM upShelfRequest WHERE userName = '{merchantName}' AND name = '{name}'"
    mutex.acquire()
    cursor.execute(transaction_ask)
    result = cursor.fetchall()
    #print(result[0]['discription'],' ',result[0]['picture'],' ',result[0]['price'],' ',result[0]['stock'])
    transaction_insert = f"insert into goodsList(merchantName,name,discription,picture,price,stock,shelf)\
        values('{merchantName}','{name}','{result[0]['discription']}','{result[0]['picture']}',\
            {result[0]['price']},{result[0]['stock']},'up')"
    cursor.execute(transaction_insert)
    conn.commit()
    mutex.release()
    return "Success"

@netshop.route("/admin/checkMCIRequest/sendBack", methods=['GET', 'POST'])
def MCIRequestsendBack():
    updateSubmitStatus("MCIRequest", "sendBack")
    return "Success"