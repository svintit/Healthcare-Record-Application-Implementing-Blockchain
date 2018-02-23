from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit
import time
#import json

bdb_root_url = 'http://127.0.0.1:9984/'
b = BigchainDB(bdb_root_url)
#generate the keys from generateKey.py
#should only run once

user_priv_key = 'A89CQNfYBBx32yY38wNLg3WkuEkG3PkCCgbJoRhsPGL1'
user_pub_key = 'DNMXVNKnLL8CwWBdeDrXBrxDSQc3jjrNVghsJbkV2gEa'
doc_pub_key = '8RqAhyuHVSnuvUTnJAe187eZkyuqMHBQSn7gbNavBnep'
#example of a record

digital_asset_payload = {
    'data': {
        'record': {
             'msg':'asset has been added to block using User Private Key and Doctor public key'
        }
    },
}

transfer_asset = {
    'id': digital_asset_payload
}

tx = b.transactions.prepare(
    operation='CREATE',
    signers=doc_pub_key,
    asset= digital_asset_payload
)

signed_tx = b.transactions.fulfill(
    tx,
    private_keys=user_priv_key
)

sent_tx = b.transactions.send(signed_tx)

tx_id = signed_tx['id']

trials = 0
while trials < 60:
    try:
        if b.transactions.status(tx_id).get('status') == 'valid':
            print('Tx valid in:', trials, 'secs')
            break
    except bigchaindb_driver.exceptions.NotFoundError:
        trials += 1
        sleep(1)

if trials == 60:
    print('Tx is still being processed... Bye!')
    exit(0)


print ("Transaction is validated")

x = b.transactions.retrieve(tx['id'])

print (x.get('asset'))
print (x.get('id'))
#returns the latest healthcare record
