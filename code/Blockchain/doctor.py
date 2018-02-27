from bigchaindb_driver.crypto import generate_keypair

class Doctor():
    doctor = generate_keypair()

    def __init__ (self):
        self.pub = doctor.public_key
        self.priv = doctor.private_key

    def getDoctorPublicKey(self):
        self.pub = doctor.public_key
        return pub

    def getDoctorPrivateKey(self):
        self.priv = doctor.private_key
        return priv
