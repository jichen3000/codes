# sudo pip install yahoo-finance
from yahoo_finance import Share

the_share = Share('')
print the_share.get_open()
print the_share.get_price()
print the_share.get_trade_datetime()