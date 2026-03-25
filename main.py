import json
import random
import string
#display functions
def display_line():
    print(f"{"-"*32}")
def display_space():
    print(f" ")    
def display_line_parameter(i):
    print(f"{"-"*i}")

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
        print(f"3. Search Account By Website")
        print(f"4. Generate Secure Password")
        print(f"5. Reset Program")
        print(f"6. Exit")
        
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
            print(f"Account added successfully!")
            display_line()
        #condition for option 2
        elif option==2:
            while True:
                display_space()
                print(f"{'Index':<12}{'Website':<12}{'Username or Email':<12}")
                index=0
                display_line_parameter(52)
                while index<len(locker):
                    print(f"{index:<12}{locker[index]['website_name']:<12}{locker[index]['username_or_email']:<12}")
                    display_line_parameter(52)
                    index+=1
                print(f"1. Show Details")
                print(f"2. Update Account Password")
                print(f"3. Delete Account")
                print(f"4. Home Menu")
                try:
                    sub_option=int(input("Choose option: "))
                except ValueError:
                    display_space()
                    print("Option must be a integer!")
                    display_line()
                    continue    
                if sub_option==1:
                    try:
                        display_space()
                        show_details=int(input("Enter index to show details: "))
                    except ValueError:
                        display_space()
                        print("index must be a integer!")
                        display_line()
                        continue    
                    if 0<=show_details<len(locker):
                        display_space()
                        print(f"Website: {locker[show_details]['website_name']}")
                        print(f"Username or Email: {locker[show_details]['username_or_email']}")
                        print(f"Password: {locker[show_details]['account_password']}")
                        display_line_parameter(42)
                        break
                    else:
                        display_space()
                        print(f"Invalid input!")
                        display_line()
                        continue
                elif sub_option==2:
                    try:    
                        display_space()
                        update_account_pass=int(input("Enter index to update account password: "))
                    except ValueError:
                        display_space()
                        print("index must be a integer!")
                        display_line()
                        continue   
                    if 0<=update_account_pass<len(locker):
                        display_space()
                        print(f"Website: {locker[update_account_pass]['website_name']}")
                        print(f"Username or Email: {locker[update_account_pass]['username_or_email']}")
                        print(f"Old Password: {locker[update_account_pass]['account_password']}")
                        updated_pass=input("Enter New Password: ")
                        locker[update_account_pass]["account_password"]=updated_pass
                        with open("locker.json","w") as file:
                            json.dump(locker,file)
                        print(f"Password updated successfully!")    
                        display_line_parameter(42)
                        break
                    else:
                        display_space()
                        print(f"Invalid input!")
                        display_line()
                        continue
                elif sub_option==3:
                    try:
                        display_space()
                        delete_account=int(input("Enter index to delete account: "))
                    except ValueError:
                        display_space()
                        print("index must be a integer!")
                        display_line()
                        continue    
                    display_space()
                    print(f"Website: {locker[delete_account]['website_name']}")
                    print(f"Username or Email: {locker[delete_account]['username_or_email']}")
                    print(f"Password: {locker[delete_account]['account_password']}")
                    check_delete_account=input("Are you sure?[y/n]: ").lower()
                    if check_delete_account=="y":
                        display_space()
                        locker.pop(delete_account)
                        with open("locker.json","w") as file:
                            json.dump(locker,file)
                        print(f"Account deleted successfully!")
                        display_line()
                        break
                    elif check_delete_account=="n":
                        continue
                    else:
                        display_space()
                        print(f"Invalid input!")
                        display_line()
                        continue   
                elif sub_option==4:
                    display_space()
                    display_line()
                    break
                else:
                    display_space()
                    print(f"Invalid input!")
                    display_line()
                    continue    

        #condition for option 3
        elif option==3:
            display_space()
            search_account=input("Enter website name to search: ").lower()
            index=0
            check=0
            while 0<=index<len(locker):
                if locker[index]["website_name"].lower()==search_account:
                    check+=1
                    display_space()
                    print(f"Website: {locker[index]['website_name']}")
                    print(f"Username or Email: {locker[index]['username_or_email']}")
                    print(f"Password: {locker[index]['account_password']}")
                    display_line_parameter(42)
                index+=1    
            if check==0:
                display_space()
                print("No match found!")
                display_line()
                break

        #condition for option 4
        elif option==4:
            random_char=string.ascii_letters+string.digits+string.punctuation
            random_password=random.choice(random_char)
            value=str()
            for item in range(1,12,1):
                value+=random_password
                random_password=random.choice(random_char)
            display_space()
            print(f"{'Index':<12}{'Website':<12}{'Username or Email':<12}")
            index=0
            display_line_parameter(52)
            while index<len(locker):
                print(f"{index:<12}{locker[index]['website_name']:<12}{locker[index]['username_or_email']:<12}")
                display_line_parameter(52)
                index+=1
            print("Random password generated!")
            try:    
                display_space()
                update_account_pass=int(input("Enter index to update account password: "))
            except ValueError:
                display_space()
                print("index must be a integer!")
                display_line()
                continue   
            if 0<=update_account_pass<len(locker):
                display_space()
                print(f"Website: {locker[update_account_pass]['website_name']}")
                print(f"Username or Email: {locker[update_account_pass]['username_or_email']}")
                print(f"Old Password: {locker[update_account_pass]['account_password']}")
                locker[update_account_pass]["account_password"]=value
                with open("locker.json","w") as file:
                    json.dump(locker,file)
                print(f"Password updated successfully!")    
                display_line_parameter(42)
            else:
                display_space()
                print(f"Invalid input!")
                display_line()
                continue

        #condition for option 5
        elif option==5:
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
                    print("Program reseted successfully!")
                    display_line()
                    break
                else:
                    display_space()
                    print(f"Authentication Failed. Incorrect password.")
                    display_line()
            break                
        #condition for option 6
        elif option==6:
            display_space()
            print("Program exited successfully!")
            display_line()
            break
        #else condition
        else:
            display_space()
            print(f"Invalid input!")
            display_line()
else:
    display_space()
    print(f"Authentication Failed. Incorrect username or password.")
    display_line()            