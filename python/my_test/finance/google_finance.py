# sudo pip install demjson
# git clone https://github.com/hongtaocai/googlefinance.git
# cd googlefinance/
# sudo python setup.py install

# getNews didn't included in the package, 
# also getNews need to limit the count
from googlefinance import getQuotes
from googlefinance import getNews
import json
print json.dumps(getQuotes('AAPL'), indent=2)
print json.dumps(getNews('AAPL'), indent=2)