import hashlib
stored_username="admin1"
stored_password="admin@123"
#SHA-256
hash_value=hashlib.sha256(stored_username.encode()).hexdigest()
hash_value1=hashlib.sha256(stored_password.encode()).hexdigest()
#take username from password
username=input("enter the username: ")
#take password from input from user
password=input("enter the password: ")
#SHA-256
hash_value2=hashlib.sha256(username.encode()).hexdigest()
hash_value3=hashlib.sha256(password.encode()).hexdigest()
if stored_username==username and stored_password==password:
        print("username and password is valid")
else:
        print("username and password is invalid")
'''print("orginal  username",stored_username)
print("original password",stored_password)'''

