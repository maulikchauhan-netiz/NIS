import hashlib


#take a password from input from user
password=input("enter the alphanumeric password: ")
#generate SHA-256 hash value
hash_value=hashlib.sha256(password.encode()).hexdigest()
#diplay result
print("\n original password",password)
print("SHA-256 hash value")
print(hash_value)
