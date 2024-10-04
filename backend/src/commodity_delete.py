from router import *

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