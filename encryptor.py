from ecies.utils import generate_eth_key
from ecies import encrypt, decrypt
import binascii
import json
import os

def save(keydict, file="keys.dat"):
    with open(file, "w") as keyfile:
        keyfile.write(json.dumps(keydict))

def load(file="keys.dat"):
    with open(file) as keyfile:
        data = json.loads(keyfile.read())
    return data

def keyfile_found(file="keys.dat"):
    if os.path.isfile(file):
        return True
    else:
        return False

def generate():
    keydict = {}
    privKey = generate_eth_key()

    keydict["private"] = privKey.to_hex()
    keydict["public"] = privKey.public_key.to_hex()

    return keydict

def encrypt_whole(pubkey, plaintext):
    encrypted = encrypt(pubkey.strip(), plaintext.encode())
    return binascii.hexlify(encrypted)

def decrypt_whole(privkey, ciphertext):
    decrypted = decrypt(privkey.strip(), binascii.unhexlify(ciphertext))
    return decrypted.decode()

if __name__ == "__main__":
    if not keyfile_found():
        keydict = generate()
        save(keydict)
    else:
        keydict = load()

    print("Encryption public key:", keydict["public"])
    print("Decryption private key:", keydict["private"])

    plaintext = 'Some plaintext for encryption'
    print("Plaintext:", plaintext)

    encrypted = encrypt_whole(keydict["public"], plaintext)
    print("Encrypted:", encrypted)

    decrypted = decrypt_whole(keydict["private"], encrypted)
    print("Decrypted:", decrypted)