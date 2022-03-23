import hashlib, binascii

text = 'exercise-cryptography'
data = text.encode("utf8")

sha256hash = hashlib.sha256(data).digest()
print("SHA256:   ", "0x" + binascii.hexlify(sha256hash).decode('utf-8'))

sha512hash = hashlib.sha512(data).digest()
print("SHA512: ", "0x" + binascii.hexlify(sha512hash).decode('utf-8'))

ripemd160 = hashlib.new('ripemd160', data).digest()
print("RIPEMD-160:", "0x" + binascii.hexlify(ripemd160).decode('utf-8')) 