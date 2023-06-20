import json

_nextOrderId = 0

class OrderList():
    def __init__(self):
        self._dict = {}
    
    def create(self, username):
        global _nextOrderId
        self._dict[str(_nextOrderId)] = {
            'username': username, 
            'orderInfo': [], 
            'payStatus': 'unpaid' # 'unpaid', 'paid', 'cancelled', 'completed'
        }
        _nextOrderId += 1
        return str(_nextOrderId - 1)
    
    def orderItem(self, orderId, goodsName, merchantName, quantity, unitPrice):
        self._dict[orderId]['orderInfo'].append({
            'goodsName': goodsName, 
            'merchantName': merchantName, 
            'quantiry': quantity, 
            'unitPrice': unitPrice
        })
    
    def getUsername(self, orderId):
        return self._dict[orderId]['username']
    
    def getTotalPrice(self, orderId):
        totalPrice = 0
        for unitPrice in self._dict[orderId]['orderInfo']:
            totalPrice += unitPrice
        return totalPrice
    
    def orderInfo(self, orderId):
        return self._dict[orderId]['orderInfo']
    
    def pay(self, orderId):
        self._dict[orderId]['payStatus'] = 'paid'
    
    def cancel(self, orderId):
        self._dict[orderId]['payStatus'] = 'cancelled'
    
    def confirm(self, orderId):
        self._dict[orderId]['payStatus'] = 'completed'

orderList = OrderList()