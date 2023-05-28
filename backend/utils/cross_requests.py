import json

class DeleteGoodRequest():
    def __init__(self):
        self._list = []
        self._proto = {
            'userName': 'seller',
            'shopName': 'seller_test_shopname',
            'name': 'seller_test_comodity',
            'discription': 'description',
            'picture': '',
            'price': 0,
            'stock': '0',
            'submitStatus': 'submitted'
        }
    
    def getAll(self):
        return self._list
    
    def insert(self, userName, shopName, name, discription, picture, price, stock):
        self._list.append({
            'userName': userName,
            'shopName': shopName,
            'name': name,
            'discription': discription,
            'picture': picture,
            'price': price,
            'stock': stock,
            'submitStatus': 'Submitted'
        })
    
    def _getIndex(self, userName, shopName, name):
        for i in range(len(self._list)):
            if self._list[i]['userName'] != userName:
                continue
            if self._list[i]['shopName'] != shopName:
                continue
            if self._list[i]['name'] != name:
                continue
            return i
    
    def agree(self, userName, shopName, name):
        i = self._getIndex(userName, shopName, name)
        self._list[i]['submitStatus'] = 'Passed'
    
    def disagree(self, userName, shopName, name):
        i = self._getIndex(userName, shopName, name)
        self._list[i]['submitStatus'] = 'sendBack'


deleteGoodRequest = DeleteGoodRequest()