from flask import Flask, request
import scrypt
import hashlib
import hmac
import binascii
import json
import os

app =Flask(__name__)

@app.route('/crypto1/sha256', methods=["POST"])
def sha256_endpoint():
    values = request.get_json()
    if not values:
        return "Missing body", 400

    required = ["msg"]
    if not all(k in values for k in required):
        return "Missing values", 400

    sha256hash = hashlib.sha256(values["msg"].encode("utf-8")).digest()

	
    response = {"hash": "0x" + sha256hash.hex()}

    return json.dumps(response), 201

@app.route('/crypto1/sha512', methods=["POST"])
def sha512_endpoint():
    values = request.get_json()
    if not values:
        return "Missing body", 400

    required = ["msg"]
    if not all(k in values for k in required):
        return "Missing values", 400
    
    sha512hash = hashlib.sha512(values["msg"].encode("utf-8")).digest()
	
    response = {"hash": "0x" + sha512hash.hex()}

    return json.dumps(response), 201

@app.route('/crypto1/ripemd160', methods=["POST"])
def ripemd160_endpoint():
    values = request.get_json()
    if not values:
        return "Missing body", 400

    required = ["msg"]
    if not all(k in values for k in required):
        return "Missing values", 400
    ripemd160hash = hashlib.ripemd160(values["msg"].encode("utf-8")).digest()
    response = {"hash": "0x" + ripemd160hash.hex()}

    return json.dumps(response), 201

@app.route('/crypto1/hmac', methods=["POST"])
def hmac_endpoint():
    values = request.get_json()
    if not values:
        return "Missing body", 400

    required = ["msg", "key"]
    if not all(k in values for k in required):
        return "Missing values", 400

    key = binascii.hexlify(b'secret')
    msg = "exercise-cryptography".encode('utf-8')

    newHMAC =hmac.new(key, msg, hashlib.sha256).digest()

    #print(newHMAC.hex())
    response = {"hmac": "0x" + newHMAC.hex()}

    return json.dumps(response), 201

@app.route('/crypto1/scrypt', methods=["POST"])
def scrypt_endpoint():
    values = request.get_json()
    if not values:
        return "Missing body", 400

    required = ["password", "salt"]
    if not all(k in values for k in required):
        return "Missing values", 400

    passwd = "secret"
    salt = os.urandom(32) 
    print("Salt: ", binascii.hexlify(salt))

    key = scrypt.hash(passwd, salt, 16384, 16, 1, 32)
    #print("Derived key: ", binascii.hexlify(key))
	
    response = {"key": "0x" + binascii.hexlify(key).decode()}

    return json.dumps(response), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

