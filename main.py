import json
#display functions
def display_line():
    print(f"{"-"*32}")
def display_space():
    print(f" ")    

#loading locker.json
with open("locker.json","r") as file:
    locker=json.load(file)

print(f"{"-"*8}Password-Manager{"-"*8}")
#app username and password registration
with open("app_login_info.json","r") as file:
    app_login_info=json.load(file)
app_login_user_name=app_login_info[0]["username"]
app_login_password=app_login_info[0]["password"]
if (app_login_user_name=="#@admin#") and (app_login_password=="#@admin#"):
    display_space()
    print(f"Welcome to Password-Manager!")
    app_login_user_name=input("Set up Username: ")
    app_login_password=input("Set up Password: ")
    app_login_info[0]["username"]=app_login_user_name
    app_login_info[0]["password"]=app_login_password
    with open("app_login_info.json","w") as file:
        json.dump(app_login_info,file)
    print("Registration Successful!")
    display_line()
#taking user input and checking username,password
app_login_user_name_input=input("Enter Username: ")
app_login_password_input=input("Enter password: ")
if (app_login_user_name==app_login_user_name_input) and (app_login_password==app_login_password_input):
    display_space()
    print(f"Welcome to Password-Manager!")
    display_line()
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
        #condition for option 1
        if option==1:
            display_space()
            website_name=input("Website Name: ")
            username_or_email=input("Username or Email: ")
            account_password=input("Password: ")
            locker.append({"website_name":website_name,"username_or_email":username_or_email,"account_password":account_password})
            with open("locker.json","w") as file:
                json.dump(locker,file)
            print("Account added successfully!")
            display_line()
        #condition for option 7
        elif option==7:
            while True:
                app_login_password_input=input("Enter password: ")
                if app_login_password_input==app_login_password:
                    display_space()
                    app_login_info[0]["username"]="#@admin#"
                    app_login_info[0]["password"]="#@admin#"
                    with open("app_login_info.json","w") as file:
                        json.dump(app_login_info,file)
                    with open("locker.json","w") as file:
                        json.dump([],file)    
                    print("Program reseted successfully! Now restart your program.")
                    display_line()
                    break
                else:
                    display_space()
                    print(f"Authentication Failed. Incorrect password.")
                    display_line()
                            
        #condition for option 8
        elif option==8:
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