from cryptography.fernet import Fernet
import dbManager
def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
def load_key():
    """
    Loads the key named `secret.key` from the current directory.
    """
    return open("secret.key", "rb").read()

def encrypt_message(message):
    """
    Encrypts a message
    """
    if dbManager.KEY=='':
        key = load_key()
    else:
        key=dbManager.KEY
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message

def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message
    """
    if dbManager.KEY == '':
        key = load_key()
    else:
        key = dbManager.KEY
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    #print(decrypted_message.decode())
    return decrypted_message

try:
    file=open('secret.key')

except:
    generate_key()