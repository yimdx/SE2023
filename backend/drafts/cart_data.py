import pymysql
from threading import Lock
from pymysql import cursors

# Database configuration
DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'db'

def connect_to_database():
    """Connect to the MySQL database."""
    connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, 
    db=DB_NAME,cursorclass=cursors.DictCursor)
    return connection
mutex = Lock()

conn = connect_to_database()
cursor = conn.cursor()

#######################goodsList/cart############insert：GoodsB###############
#insert
'''
INSERT INTO goodsList(merchantName,name,discription,
picture,price,stock,shelf) VALUES('seller','GoodsC',
'测试用商品。(suitable)','file:///D:/SE/intro.jpg',1,1,'down');

transaction_goodsList = f"INSERT INTO goodsList({'merchantName'},{'name'},{'discription'},\
{'picture'},{'price'},{'stock'},{'shelf'}) VALUES('seller','GoodsB',\
'测试用商品。(suitable)','file:///D:/SE/intro.jpg',1,1,'down')"
mutex.acquire()
cursor.execute(transaction_goodsList)
conn.commit()
mutex.release()
'''

'''
transaction_goodsList = f"INSERT INTO goodsList({'merchantName'},{'name'},{'discription'},\
{'picture'},{'price'},{'stock'},{'shelf'}) VALUES('seller','GoodsB',\
'测试用商品。(suitable)','file:///D:/SE/intro.jpg',1,1,'down')"
transaction_cart = f"INSERT INTO cart({'buyerName'},{'merchantName'},{'goodsName'},\
{'picture'},{'unitPrice'},{'quantity'},{'shelf'}) VALUES('buyer','seller','GoodsB',\
'file:///D:/SE/intro.jpg',1,1,'No')"
mutex.acquire()
cursor.execute(transaction_goodsList)
conn.commit()
cursor.execute(transaction_cart)
conn.commit()
mutex.release()
'''
#select
'''
mutex.acquire()
name = "GoodsB"
goodsName = "GoodsB"
select_goodsList = f"SELECT * FROM goodsList where name='{name}'"
cursor.execute(select_goodsList)
print(cursor.fetchall())
select_cart = f"SELECT * FROM cart where goodsName='{goodsName}'"
cursor.execute(select_cart)
print(cursor.fetchall())
mutex.release()
'''

#delete
'''
mutex.acquire()
merchantName = "seller"
goodsName = "GoodsB"
delete_cart = f"delete from cart where goodsName='{goodsName}'"
cursor.execute(delete_cart)
conn.commit()
select_cart = f"SELECT * FROM cart where goodsName='{goodsName}'"
cursor.execute(select_cart)
print(cursor.fetchall())
mutex.release()
'''

#summary
'''
transaction_cart = f"INSERT INTO cart({'buyerName'},{'merchantName'},{'goodsName'},\
{'picture'},{'unitPrice'},{'quantity'},{'shelf'}) VALUES('buyer','seller','GoodsB',\
'file:///D:/SE/intro.jpg',1,1,'No')"
merchantName = "seller"
goodsName = "GoodsB"
mutex.acquire()
cursor.execute(transaction_cart)
conn.commit()
select_cart = f"SELECT * FROM cart where goodsName='{goodsName}'"
cursor.execute(select_cart)
print(cursor.fetchall())
update_cart = f"update cart set quantity=0,shelf='down' where merchantName='seller' and buyerName='buyer'"
cursor.execute(update_cart)
conn.commit()
select_cart = f"SELECT * FROM cart where goodsName='{goodsName}'"
cursor.execute(select_cart)
print(cursor.fetchall())
delete_cart = f"delete from cart where goodsName='{goodsName}'"
cursor.execute(delete_cart)
conn.commit()
select_cart = f"SELECT * FROM cart where goodsName='{goodsName}'"
cursor.execute(select_cart)
print(cursor.fetchall())
mutex.release()


'''
'''
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

def updateQuantity(formerQuantity,quantity,buyerName,merchantName,goodsName):
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
    
formerQuantity = askForQuantity('buyer','seller','goodsB')    
print(formerQuantity)
#updateQuantity(formerQuantity,1,'buyer','seller','goodsC')
#print(askForQuantity('buyer','seller','goodsC'))
'''

#shut down mysql
cursor.close()
conn.close()