print("Welcome to the Team Project Repository")

def login(username, password):
    if username == "admin" and password == "123":
        return "Login Successful"
    else:
        return "Login Failed"

print(login("admin", "123"))
print("Version B - Improved login system")
