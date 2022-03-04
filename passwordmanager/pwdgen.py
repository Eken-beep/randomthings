# Imports
import os
import sys
import random

# View passwords section
def pwdmenu():
    with open('passwords.txt', 'r') as passwords:
        pwds = passwords.read()
        print("")
        print(pwds)
        return

# Create password section
def pwdnew():
    with open('passwords.txt', 'a') as passwords:
        newuname = str(input("Enter a username for your new password: "))
        newpwd = str(input("Enter your new password: "))

        loginid = ('Username: "'+newuname+'", Password: "'+newpwd+'"\n')
        passwords.writelines(loginid)
    return

# Generate password section
def pwdgen():
    return

def pwdclear():
    print("")
    rusure = str(input("Are you sure you want to delete all passwords, [Y/N]: "))
    while True:
        if rusure == "Y" or "y":
            with open('passwords.txt', 'w') as passwords:
                passwords.writelines("")
            break
        elif rusure == "N" or "n":
            print("")
            print("Continuing without clearing password data...")
            break
        else:
            print("Invalid option...")

def mpwdclear():
    print("")
    newmpwd = str(input("Enter a new masterpassword: "))
    with open('masterpassword.txt', 'w') as new_masterpassword:
        new_masterpassword.write(newmpwd)
 
# Main menu section
def menu():
    while True:
        print("")
        print("Options:")
        print("[1] View your current passwords")
        print("[2] Create a new password")
        print("[3] Generate a new password")
        print("[4] Clear password list")
        print("[5] Reset master password")
        print("[6] Exit")
        option = int(input(": "))

        if option == 1:
            pwdmenu()
        elif option == 2:
            pwdnew()
        elif option == 3:
            pwdgen()
        elif option == 4:
            pwdclear()
        elif option == 5:
            mpwdclear()
        elif option == 6:
            quit()
        else:
            print("invalid option...")
            return


# Master password section
with open('masterpassword.txt', 'r+') as mpassword:
    mpasswd = mpassword.read()

    while True:
        if mpasswd == "":
            mpasswordinput = str(input("Enter a new masterpassword: "))
            mpassword.write(mpasswordinput)
            break
        else:
            break

    mpass = mpasswd

    # Login section
    while True:
        attempt = str(input("Login with your masterpassword: "))

        if attempt == mpass:
            menu()
            mpassword.close()
            os.system("clear")
            break

        else:
            print("Wrong password try again")
            print("")
 

