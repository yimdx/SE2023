from router import *

################################################# Seller Commodity #################################################
# def getGoodsList(): #get its name
#     userName = request.json.get('userName')
#     formName = 'goodsListOf' + userName
#     return formName

@netshop.route("/merchant/goodsList", methods=['GET', 'POST'])
def goodsList():
    #"userName" needs to be cached after login
    formName = "goodsList"
    merchantName = request.json.get('userName')
    mutex.acquire()
    transaction = f"SELECT * FROM {formName} where merchantName='{merchantName}'"
    #print(f"###########{transaction}###########")
    cursor.execute(transaction)
    result = cursor.fetchall()
    mutex.release()
    return jsonify(result=result),200
    #front end should update the filename here 

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