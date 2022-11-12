#create a private key and public key pair
from Crypto.PublicKey import RSA
import encrypt

def generateKeys():
    #if private key and public key already exist, do not generate new ones
    try:
        with open("private.pem", "r") as f:
            print("Private key already exists")
    except FileNotFoundError:
        #generate private key and public key
        key = RSA.generate(2048)
        private_key = key.export_key()
        file_out = open("private.pem", "wb")
        file_out.write(private_key)
        file_out.close()

        public_key = key.publickey().export_key()
        file_out = open("mypublickey.pem", "wb")
        file_out.write(public_key)
        file_out.close()


#main function
def main(action, message, filename=None):
    generateKeys()

    if(action == "encrypt"):
        with open(filename, "rb") as f:
            public_key = RSA.import_key(f.read())
        encrypted = encrypt.encrypt(message, public_key)
        encrypted = encrypted.hex()
        print(encrypted)

    elif(action == "decrypt"):
        with open("private.pem", "rb") as f:
            private_key = RSA.import_key(f.read())
        encrypted = bytes.fromhex(message.decode())

        decrypted = encrypt.decrypt(encrypted, private_key)
        print(decrypted)

if __name__ == "__main__":
    #get arugments from command line
    import sys
    action = sys.argv[1]
    message = sys.argv[2]
    filename = sys.argv[3]
    main(action, message.encode('utf-8'), filename)