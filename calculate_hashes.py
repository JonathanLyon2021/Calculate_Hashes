import hashlib, binascii

text = 'hello world'
data = text.encode("utf8")

sha256hash = hashlib.sha256(data).digest()
print("SHA256:   ", binascii.hexlify(sha256hash))

sha512 = hashlib.sha512(data).digest()
print("SHA512: ", binascii.hexlify(sha512))

ripemd160 = hashlib.new('ripemd160', data).digest()
print("RIPEMD-160:", binascii.hexlify(ripemd160)) 