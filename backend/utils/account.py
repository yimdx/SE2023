import json

class Account():
    def __init__(self):
        self._dict = {}
        self._dict['admin'] = {
            'password': '_qwe123',
            'userType': 'admin', 
            'idNumber': '0',
            'phoneNumber': '00000000',
            'email': "admin@gmail.com",
            'balance': 0
        }
        self._dict['buyer'] = {
            'password': '_qwe123',
            'userType': 'buyer', 
            'idNumber': '0',
            'phoneNumber': '00000000',
            'email': "buyer@gmail.com",
            'balance': 0
        }
        self._dict['seller'] = {
            'password': '_qwe123',
            'userType': 'seller', 
            'idNumber': '0',
            'phoneNumber': '00000000',
            'email': "seller@gmail.com", 
            'balance': 0
        }
    
    def _remove(self, oldUserName):
        del self._dict[oldUserName]
    
    def _alter(self, username, password, userType, idNumber, phoneNumber, email, balance=0):
        self._dict[username] = {
            'password': password,
            'userType': userType, 
            'idNumber': idNumber,
            'phoneNumber': phoneNumber,
            'email': email, 
            'balance': balance
        }
    
    def insert(self, username, password, userType, idNumber, phoneNumber, email) -> bool:
        if username in self._dict:
            print(f'Account insertion failure: username {username} already exists.')
            return False
        self._alter(username, password, userType, idNumber, phoneNumber, email)
        return True
    
    def change(self, oldUserName, newUserName, password, phoneNumber, email) -> str:
        if oldUserName not in self._dict:
            print(f'Account change failure: old username {oldUserName} does not exist.')
            return 'username not exist'
        for key, value in self._dict.items():
            if newUserName == oldUserName:
                continue
            if newUserName == key: 
                print(f'Account change failed: new username {newUserName} already exists.')
                return 'username replicated'
            if self._dict[oldUserName]['phoneNumber'] == value['phoneNumber']:
                print(f'Account change failed: phoneNumber {phoneNumber} is the same with {key}.')
                return 'phoneNumber replicated'
            if self._dict[oldUserName]['email'] == value['email']:
                print(f'Account change failed: email {email} is the same with {key}.')
                return 'email replicated'
        userType = self._dict[oldUserName]['userType']
        idNumber = self._dict[oldUserName]['idNumber']
        balance = self._dict[oldUserName]['balance']
        self._remove(oldUserName)
        self._alter(newUserName, password, userType, idNumber, phoneNumber, email, balance)
        return 'Success'
    
    def query(self, username) -> dict:
        res = self._dict[username]
        res['username'] = username
        return res
    
    def queryOnSecondaryKey(self, keyname, keyvalue):
        for key, value in self._dict.items():
            if value[keyname] == keyvalue:
                return self.query(key)
    
    def recharge(self, username, value):
        if username not in self._dict:
            print(f'Account recharge failure: username {username} does not exist')
            return False
        self._dict[username]['balance'] += value
        return True
    
    def charge(self, username, value):
        if username not in self._dict:
            print(f'Account charge failure: username {username} does not exist')
            return False
        self._dict[username]['balance'] -= value
        return True
    
    def auth(self, username, password) -> bool:
        if username not in self._dict:
            print(f'Account auth failure: username {username} does not exist')
            return False
        if self._dict[username]['password'] != password:
            print(f'Account auth failure: password {password} for user {username} \
                  does not match {self._dict[username]["password"]}')
            return False
        return True

class AdminAccounts():
    def __init__(self):
        self._profitAccount = {
            "account": 'adminProfitAccount',
            "balance": 0
        }
        self._medianAccount = {
            "account": 'adminMedianAccount',
            "balance": 0
        }
    
    def profitAccountRecharge(self, value):
        self._profitAccount['balance'] += value
    
    def medianAccountRecharge(self, value):
        self._medianAccount['balance'] += value
    
    def profitAccountCharge(self, value):
        self._profitAccount['balance'] -= value
    
    def medianAccountCharge(self, value):
        self._medianAccount['balance'] -= value
    
    def profitAccountShow(self):
        return self._profitAccount
    
    def medianAccountShow(self):
        return self._medianAccount

account = Account()
adminAccounts = AdminAccounts()