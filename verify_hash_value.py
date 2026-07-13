import hashlib
#input
message="cyber security is the most important"
#generate SHA-hash value.
original_hash=hashlib.sha3_256(message.encode()).hexdigest()
print("original message",message)
print("original SHA-3 Hash",original_hash)
#verify data integrity
received_value=input("\n enter the received value: ")
received_value=hashlib.sha3_256(received_value.encode()).hexdigest()
if original_hash==received_value:
    print("data integrity is verified:the received data is unchanged")
else:
    print("data integrity is verified:the received data is changed")  