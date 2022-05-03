import time

username="sreeram"
password="secrsreeetpass"

Username=input("Enter username")
Password=input("Enter password")
if Username==username and Password==password:
    print("Access granted")
    time.sleep(2)
    print("You are successfully logged in")
elif Username!=username and Password==password:
    print("Username is incorrect")
elif Username==username and Password!=password:
    print("Password is incorrect")
else:
    print("Please check both inputs")