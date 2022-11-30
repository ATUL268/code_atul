import pyotp
from kite_trade import *
import pdb


secret_key_DA3168 = "M6T4JEDJ4L53DHTVQRXZPU3OHDZ3MT7Y"
totp_DA3168 = pyotp.TOTP(secret_key_DA3168).now()
totp_DA3168 = str(totp_DA3168)
print(totp_DA3168) 

user_id = "DA3168"       # Login Id
password = "Share@077"      # Login password
twofa = totp_DA3168        # Login Pin or TOTP

enctoken = get_enctoken(user_id, password, twofa)
kite = KiteApp(enctoken=enctoken)

while True:
	print(kite.ltp('NSE:SBIN')['NSE:SBIN']['last_price'])








# pdb.set_trace()

# print(kite.positions())
# order = kite.place_order(variety=kite.VARIETY_REGULAR,
#                          exchange=kite.EXCHANGE_NSE,
#                          tradingsymbol="IDEA",
#                          transaction_type=kite.TRANSACTION_TYPE_SELL,
#                          quantity=1,
#                          product=kite.PRODUCT_MIS,
#                          order_type=kite.ORDER_TYPE_MARKET,
#                          price=None,
#                          validity=None,
#                          disclosed_quantity=None,
#                          trigger_price=None,
#                          squareoff=None,
#                          stoploss=None,
#                          trailing_stoploss=None,
#                          tag="TradeViaPython")





# secret_key_IQL773 =  "5X43YYRJ34GHZXEB555SSPOMBNMSMBG4"
# totp_IQL773 = pyotp.TOTP(secret_key_IQL773).now()
# totp_IQL773 = str(totp_IQL773)
# print(totp_IQL773)





# # First Way to Login
# # You can use your Kite app in mobile
# # But You cname = "SBIN"
# pdb.set_trace()



# ----------------------------


# user_id_1 = "DA3168"       # Login Id
# password_1 = "Share@077"      # Login password
# twofa_1 = totp_DA3168  
# secret_key_IQL773 =  "5X43YYRJ34GHZXEB555SSPOMBNMSMBG4"
# totp_IQL773 = pyotp.TOTP(secret_key_IQL773).now()
# totp_IQL773 = str(totp_IQL773)
# # print(totp_IQL773)
# enctoken = get_enctoken(user_id, password, twofa)
# kite = KiteApp(enctoken=enctoken)















# Cancel order
# kite.cancel_order(variety=kite.VARIETY_AMO,
#                   order_id="221123202001315")

# user_id = "IQL773"       # Login Id
# password = "Share@077"      # Login password
# twofa = totp_IQL773        # Login Pin or TOTP
# # pdb.set_trace()

# enctoken = get_enctoken(user_id, password, twofa)
# kite = KiteApp(enctoken=enctoken)

# print(kite.positions())



# order = kite.place_order(variety=kite.VARIETY_REGULAR,
#                          exchange=kite.EXCHANGE_NSE,
#                          tradingsymbol="ACC",
#                          transaction_type=kite.TRANSACTION_TYPE_BUY,
#                          quantity=1,
#                          product=kite.PRODUCT_MIS,
#                          order_type=kite.ORDER_TYPE_MARKET,
#                          price=None,
#                          validity=None,
#                          disclosed_quantity=None,
#                          trigger_price=None,
#                          squareoff=None,
#                          stoploss=None,
#                          trailing_stoploss=None,
#                          tag="TradeViaPython")



# # kite.modify_order(variety=kite.VARIETY_REGULAR,
#                   order_id="order_id",
#                   parent_order_id=None,
#                   quantity=5,
#                   price=200,
#                   order_type=kite.ORDER_TYPE_LIMIT,
#                   trigger_price=None,
#                   validity=kite.VALIDITY_DAY,
#                   disclosed_quantity=None)


