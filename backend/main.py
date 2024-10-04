from router import *
import src.cart
import src.commodity_admin
import src.commodity_seller
import src.commodity_delete
import src.registration_login
import src.shop_opening
import src.user_account
import src.user_order

if __name__ == "__main__":
    try:
        netshop.run(host="127.0.0.1", port=3000, debug=True)
    finally:
        #shut down MySQL
        cursor.close()
        conn.close()