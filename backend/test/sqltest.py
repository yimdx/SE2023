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


'''
formName = "goodsList"
mutex.acquire()
transaction = f"select shelf from {formName} where name='GoodsB'"
cursor.execute(transaction)
result = cursor.fetchall()
mutex.release()
if not result[0]:
    print("null")
print(result[0]['shelf'])   

cartName = 'cart'
buyerName = 'buyer'#!
mutex.acquire()
transaction = f"select * from {cartName} where buyerName='{buyerName}' "#!
cursor.execute(transaction)
preResult = cursor.fetchall()
print(f"###############preResult={preResult}############")
mutex.release()
for tpl in preResult:
    goodsStatus = "No"
    insertStr = f"update {cartName} set shelf='{goodsStatus}' \
    where goodsName='{tpl['goodsName']}'" #!复制粘贴
    mutex.acquire()
    cursor.execute(insertStr)
    conn.commit()
    mutex.release()
mutex.acquire()
cursor.execute(transaction)
result = cursor.fetchall()
print(f"###############result={result}############")
mutex.release()
'''
'''USR
merchantName = 'seller'
name = 'GoodsC'
transaction_ask = f"SELECT userName, name, discription, \
        picture, price, stock FROM upShelfRequest WHERE userName = '{merchantName}' AND name = '{name}'"
mutex.acquire()
cursor.execute(transaction_ask)
result = cursor.fetchall()
print(result[0]['discription'],' ',result[0]['picture'],' ',result[0]['price'],' ',result[0]['stock'])
transaction_insert = f"insert into goodsList(merchantName,name,discription,picture,price,stock,shelf)\
        values('{merchantName}','{name}','{result[0]['discription']}','{result[0]['picture']}',\
            {result[0]['price']},{result[0]['stock']},'up')"
cursor.execute(transaction_insert)
conn.commit()

mutex.release()
'''



cursor.close()
conn.close()
