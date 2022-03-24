import hashlib, hmac, binascii     

#def hmac_sha256(key, msg):
#   return hmac.new(key, msg, hashlib.sha256).digest()

key = binascii.hexlify(b'secret')
msg = "exercise-cryptography".encode('utf-8')

newHMAC =hmac.new(key, msg, hashlib.sha256).digest()

print(newHMAC.hex())