import json
#display functions
def display_line():
    print(f"{"-"*32}")
def display_space():
    print(f" ")    

#app username and password registration
with open("app_login_info.json","r") as file:
    app_login_info=json.load(file)
app_login_user_name=app_login_info[0]["username"]
app_login_password=app_login_info[0]["password"]
if (app_login_user_name=="admin") & (app_login_password=="admin"):
    print(f"Welcome to Password-Manager!")
    app_login_user_name=input("Set up Username: ")
    app_login_password=input("Set up Password: ")
    app_login_info[0]["username"]=app_login_user_name
    app_login_info[0]["password"]=app_login_password
    print(app_login_info)
    with open("app_login_info.json","w") as file:
        json.dump(app_login_info,file)
    print("Registration Successful!")

#taking user input and checking username,password
app_login_user_name_input=input("Enter Username: ")
app_login_password_input=input("Enter password: ")
if (app_login_user_name==app_login_user_name_input) & (app_login_password==app_login_password_input):
    print(f"{"-"*8}Password-Manager{"-"*8}")
    while True:
        #Program menu design
        print(f"1. Add New Account")
        print(f"2. View All Saved Accounts")
        print(f"3. Update Account Password")
        print(f"4. Search Account By Website")
        print(f"5. Delete Account")
        print(f"6. Generate Secure Password")
        print(f"7. Reset Program")
        print(f"8. Exit")
        #choose option
        try:
            option=int(input("Choose Option: "))
        except ValueError:
            display_space()
            print(f"Invalid input!")
            display_line()
            continue    
        #if else condition for option 8
        if option==8:
            display_space()
            print("Program exited successfully!")
            display_line()
            break
        else:
            display_space()
            print(f"Invalid input!")
            display_line()
else:
    display_space()
    print(f"Authentication Failed. Incorrect username or password.")
    display_line()            