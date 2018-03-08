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

user_priv_key = 'BSCuLz8f65KGtz3dAxLRG9CP3cagpmpCJJDmC3rqxDfX'
user_pub_key = '138dsEMVq1RYABi9K2BunGsEgbgyaA86FjC3XTYBdSZd'

#example of a record
digital_asset_payload = {
    'data': {
        'record': {
            'test':'hello djongo',
            'is it working':'maybe'
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

print (x.get('asset'))
print (x.get('id'))
#returns the latest healthcare record

#Now to give access to the doctor to view it
transfer_asset = {
    'id': tx_id
}
output_index = 0
output = signed_tx['outputs'][output_index]

transfer_input = {
    'fulfillment': output['condition']['details'],
    'fulfills': {
        'output_index': output_index,
        'transaction_id': tx_id
    },
    'owners_before': output['public_keys'],

}

doc_pub_key = 'B3zL5ch5qi68XwMGC94GPGPv9P8WdXF9GZGt4xdHwcyS'

prepared_transfer = b.transactions.prepare(
    operation = 'TRANSFER',
    asset = transfer_asset,
    inputs = transfer_input,
    recipients= doc_pub_key
)

signed_transfer = b.transactions.fulfill(
    prepared_transfer,
    private_keys = user_priv_key
)

sent_transfer = b.transactions.send(signed_transfer)

print(sent_transfer.get('id'))
