from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

#Run this once
doc_priv = generate_keypair()
private = doc_priv.private_key
public = doc_priv.public_key
#print("Your public key is: " +public)
#print("Your private key is: " +private)
