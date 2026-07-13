import hashlib
#input
message="cyber security is the most important for protecting digital information"
#generate SHA-hash value.
hash_value=hashlib.sha3_256(message.encode())
#display
print("input message")
print(message)
print("\n SHA-3 hash value : ")
print(hash_value.hexdigest())