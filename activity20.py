from getpass import getpass

i = "toto"
g = "buday"

isLogin = False #trigger

while isLogin == False:
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    if username == i and password == g:
        print("Login successful")
        isLogin = True
    else:
        print("Invalid username or password. Please try again.")
    