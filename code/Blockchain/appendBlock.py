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

user_priv_key = '3TJJvXsvLbjQoFDbtSi2gjMmHu3jb9CE81PS5WFMfrxy'
user_pub_key = 'GororGhkaDuW7uWirKpjxPjkKMAshwJYqzt4xSdAFgG2'

#example of a record
digital_asset_payload = {
    'data': {
        'details': {
            'Name':'Geraldine Murphy',
            'Address':'742 Evergreen Terrace, Springfield',
            'Phone num': '12345123',
            'Emergency Contact': '0876923528',
            'PPSN':'12345789W',
            'Previous Doctors' : 'Andrew Wong, Matthew McConaughey',
            'Illness':'Tuberculosis'
        }
    },
}

transfer_asset = {
    'id': digital_asset_payload
}



tx = b.transactions.prepare(
    operation='CREATE',
    signers=user_pub_key,
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

print (x.get('data'))
print (x.get('id'))
#returns the latest healthcare record
