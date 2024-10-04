from router import *

################################################# Order #################################################

@netshop.route("/buyer/order/create", methods=['POST', 'GET'])
def buyer_order_create():
    username = request.json.get('username')
    orderId = orderList.create(username)
    return {'orderId': orderId}

@netshop.route("/buyer/order/orderItem", methods=['POST', 'GET'])
def buyer_order_orderItem():
    orderId = request.json.get('orderId')
    goodsName = request.json.get('goodsName')
    merchantName = request.json.get('merchantName')
    quantity = request.json.get('quantity')
    unitPrice = request.json.get('unitPrice')
    orderList.orderItem(orderId, goodsName, merchantName, quantity, unitPrice)
    return 'Success', 200

@netshop.route("/buyer/order/orderInfo", methods=['POST', 'GET'])
def buyer_order_orderInfo():
    orderId = request.json.get('orderId')
    return jsonify(orderList.orderInfo(orderId))

@netshop.route("/buyer/order/pay", methods=['POST', 'GET'])
def buyer_order_pay():
    orderId = request.json.get('orderId')
    orderList.pay(orderId)
    
    username = orderList.getUsername(orderId)
    totalPrice = orderList.getTotalPrice(orderId)
    account.charge(username, totalPrice)
    adminAccounts.medianAccountRecharge(totalPrice)
    return 'Success', 200