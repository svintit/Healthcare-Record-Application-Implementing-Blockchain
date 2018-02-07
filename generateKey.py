from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair

#Run this once
user_priv = generate_keypair()
private = user_priv.private_key
public = user_priv.public_key
print("Your private key is: " +private)
print("Your public key is: " +public)
