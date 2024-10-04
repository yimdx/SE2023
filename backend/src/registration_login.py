from router import *

################################################# Registration #################################################
@netshop.route("/register", methods=['POST', 'GET'])
def userAccountRegistration():
    username = request.json.get('username')
    password = request.json.get('password')
    userType = request.json.get('userType')
    idNumber = request.json.get('idNumber')
    phoneNumber = request.json.get('phoneNumber')
    email = request.json.get('email')
    if account.insert(username, password, userType, idNumber, phoneNumber, email):
        return ("OK", 200)
    else:
        print('userAccountRegistration failure')
        return ("RegistrationFailed", 201)

################################################# Login #################################################

def generalLogin() -> str:
    username = request.json.get('username')
    password = request.json.get('password')
    # print(username, password, str(account.auth(username, password)))
    if account.auth(username, password):
        return "Success", 200
    else: 
        return "AuthenticationFailed", 201

@netshop.route("/admin/login", methods=['POST', 'GET'])
def adminLogin():
    return generalLogin()

@netshop.route("/buyer/login", methods=['POST', 'GET'])
def buyerLogin():
    return generalLogin()

@netshop.route("/seller/login", methods=['POST', 'GET'])
def sellerLogin():
    return generalLogin()