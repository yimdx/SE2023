from flask import Flask, jsonify, redirect, render_template, request, session, url_for
import pymysql
from pymysql import cursors
from flask_caching import Cache
from threading import Lock

from utils.check_validity import checkIID, checkCommodityInfo
from utils.account import account, adminAccounts
from utils.cross_requests import deleteGoodRequest
from utils.order import orderList

netshop = Flask(__name__)
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', 
                       passwd='123456', charset='utf8', db='db',cursorclass=cursors.DictCursor)
mutex = Lock()
cursor = conn.cursor()

# jwt = JWTManager(netshop)
cache = Cache(config={"CACHE_TYPE": "simple"})
cache.init_app(netshop)


@netshop.route("/test")
def testAccessibility():
    return "Hello from backend!"