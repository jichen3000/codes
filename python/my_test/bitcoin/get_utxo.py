import json
import requests
# The API URL is https://blockchain.info/unspent?active=<address>
# It returns a JSON object with a list "unspent_outputs", containing UTXO, like this:
#{ "unspent_outputs":[
#{
# "tx_hash":"ebadfaa92f1fd29e2fe296eda702c48bd11ffd52313e986e99ddad9084062167", # "tx_index":51919767,
# "tx_output_n": 1,
# "script":"76a9148c7e252f8d64b0b6e313985915110fcfefcf4a2d88ac",
#     "value": 8000000,
#     "value_hex": "7a1200",
#     "confirmations":28691
#   },
# ...

def main(address):
    response = requests.get('https://blockchain.info/address/{address}'.format(
            address=address))
    response.text.pp()
    # utxo_set = json.loads(response.text).pp()

if __name__ == '__main__':
    from minitest import *

    with test(main):
        main("1Exfso2kzXWNbng3UQuqprAWAuSE1Tfx4b")