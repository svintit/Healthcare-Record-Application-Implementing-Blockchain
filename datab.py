from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit
import time

bdb_root_url = 'http://127.0.0.1:9984/'
b = BigchainDB(bdb_root_url)

user_priv = generate_keypair()
uer_pub = generate_keypair()

digital_asset_payload = {
    'data': {'msg': 'This is my special message just for you'}
}


transfer_asset = {
    'id': digital_asset_payload
}

tx = b.transactions.prepare(
    operation='CREATE',
    signers=user_priv.public_key,
    asset= digital_asset_payload
)

signed_tx = b.transactions.fulfill(
    tx,
    private_keys=user_priv.private_key
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

print("almost there")
tx_retrieved = b.transactions.retrieve(tx['id'])
#txid = fulfilled_creation_tx['id']



#sent_transfer_tx = b.transactions.send(fulfilled_transfer_tx)

print ("Transaction is validated")

#time.sleep(2)
x = b.transactions.retrieve(tx['id'])
#tx_retrieved = b.transactions.retrieve(fulfilled_creation_tx['id'])
print(x)
