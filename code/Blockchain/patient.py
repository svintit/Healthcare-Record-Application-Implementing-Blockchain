from bigchaindb_driver.crypto import generate_keypair

class Patient:
    def __init__(self, patientPubKey, patientPrivKey):
        self.patientPubKey = patientPubKey
        self.patientPrivKey = patientPrivKey

    def getKeys(self):
        patient = generate_keypair()
        patientPubKey = patient.public_key
        patientPrivKey = patient.private_key
