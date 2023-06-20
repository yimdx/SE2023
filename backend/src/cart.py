from router import *

def askForGoodsStatus(merchantName,goodsName):
    formName = "goodsList"
    mutex.acquire()
    transaction = f"select shelf from {formName} where merchantName = '{merchantName}' \
        and name='{goodsName}'"
    cursor.execute(transaction)
    result = cursor.fetchall()
    mutex.release()
    if not result[0]:
        return None # This goods didn't exist.
    return result[0]['shelf'] 

def askForQuantity(buyerName,merchantName,goodsName):
    mutex.acquire()
    transaction = f"SELECT quantity FROM cart WHERE goodsName ='{goodsName}'\
    AND buyerName = '{buyerName}' AND merchantName = '{merchantName}'"
    cursor.execute(transaction)
    result = cursor.fetchall()
    if not result:
        quantity = 0 
    else:
        quantity = result[0]['quantity']
    mutex.release()
    return quantity

def updateQuantity(quantity,buyerName,merchantName,goodsName):
    formerQuantity = askForQuantity(buyerName,merchantName,goodsName)
    total = quantity + formerQuantity
    mutex.acquire()
    if total < 1:
        transaction = f"delete from cart where \
    buyerName='{buyerName}' and goodsName='{goodsName}' and merchantName = '{merchantName}'"
        cursor.execute(transaction)
        conn.commit()
        mutex.release()
        return 0
    else:
        transaction = f"update cart set quantity={total} where \
        goodsName ='{goodsName}' and buyerName = '{buyerName}' and merchantName = '{merchantName}'" 
        cursor.execute(transaction)
        conn.commit()
        mutex.release()
        return 1
    #"update success"=1 "goods deleted"=0

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
        goodsStatus = askForGoodsStatus(tpl['merchantName'],tpl['goodsName'])
        insertStr = f"update {cartName} set shelf='{goodsStatus}' \
    where merchantName={tpl['merchantName']} and goodsName='{tpl['goodsName']}'"
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
    formerQuantity = askForQuantity(buyerName,merchantName,goodsName)
    if formerQuantity == 0:
        mutex.acquire()
        insertStr = f"insert into cart(buyerName,merchantName, goodsName, picture, \
    unitPrice, quantity) values({buyerName},{merchantName}, {goodsName}, \
    {picture}, {unitPrice}, {quantity})"
        cursor.execute(insertStr)
        conn.commit()
        mutex.release()
    else:
        updateQuantity(formerQuantity, quantity, buyerName,merchantName,goodsName)
    return "Success"

@netshop.route("/user/cart/delete", methods=['GET', 'POST'])
def deleteFromCart():
    buyerName = request.json.get("buyerName")
    merchantName = request.json.get("merchantName")
    goodsName = request.json.get("goodsName")
    mutex.acquire()
    insertStr = f"delete from cart where \
    buyerName='{buyerName}' and merchantName='{merchantName}' and goodsName='{goodsName}'"
    cursor.execute(insertStr)
    conn.commit()
    mutex.release()
    
@netshop.route("/user/cart/changeQuantity", methods=['GET', 'POST'])
def changeQuantity():
    buyerName = request.json.get("buyerName")
    merchantName = request.json.get("merchantName")
    goodsName = request.json.get("goodsName")
    quantity = request.json.get("quantity")
    if updateQuantity(quantity, buyerName,merchantName,goodsName):
        return 'Success'
    else:
        return jsonify('Deleted')