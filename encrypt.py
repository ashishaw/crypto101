from Crypto.Cipher import PKCS1_OAEP


def encrypt(message, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = cipher.encrypt(message)
    return encrypted

def decrypt(encrypted, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    decrypted = cipher.decrypt(encrypted)
    return decrypted