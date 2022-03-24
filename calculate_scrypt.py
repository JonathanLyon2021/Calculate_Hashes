import scrypt, os, binascii 

passwd = "secret"
salt = os.urandom(32) 
print("Salt: ", binascii.hexlify(salt))

key = scrypt.hash(passwd, salt, 16384, 8, 1, 32)
print("Derived key: ", binascii.hexlify(key))