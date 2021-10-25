#!/usr/bin/env python3.6
from locker import User
from locker import Credentials

def create_user(username,password):
    """
    function to create a new user
    """
    new_user = User(username,password)
    return new_user

def save_user(user):
    """
    function to save user
    """
    user.save_user()    

def delete_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def create_creds(acc_name,user_name,email,password):
    """
    function to create new account credentials
    """    
    new_account = Credentials(acc_name,user_name,email,password)
    return new_account

def save_acc(credentials):
    """
    function to save account credentials
    """
    credentials. save_user_account()

def del_account(credentials):
    """
    function to delete account credentials
    """
    credentials.delete_user_account()

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Credentials.display_accounts()




def main():
    print("Hello and  Welcome to password locker app. What is your name?")
    user_name = input()
    print ("\n")

    print("Set password for you locker app")
    password = input()
    print ("\n")

    print("Please login to your account")
    print ("\n")

    print("Enter username")
    username = input()
    print("\n")

    print("Enter password")
    pword = input()
    print("\n")

    if username == user_name and pword == password:

      print(f"Hello {user_name}. What would you like to do?")
      print("\n")

      while True:
            print("Use these short codes : a~acc - add existing account credentials , c~acc - create new account credentials, d~acc - display accounts, del~acc - delete account, exit -exit the accounts list ")
            short_code = input().lower()
            if short_code == 'a~acc':
                print("Add existing account credentials")
                print("-"*10)

                print("Account name ....")
                a_name = input()

                print("User name .....")
                u_name = input()

                print("Login Email address")
                e_address = input()

                print("Login password")
                l_password = input()


                save_acc(create_creds(a_name,u_name,e_address,l_password))
                print ("\n")
                print(f"Account {a_name} {u_name} {e_address} {l_password} added successfully")
                print("\n")

            elif short_code == 'c~acc':
                print("Create new account credentials")
                print("-"*10)

                print("Account name ....")
                a_name = input()

                print("User name .....")
                u_name = input()

                print("Login Email address")
                e_address = input()

                print("Login password")
                l_password = input()


                save_acc(create_creds(a_name,u_name,e_address,l_password))
                print ("\n")
                print(f"Account {a_name} {u_name} {e_address} {l_password} added successfully")
                print("\n")

            elif short_code == 'd~acc':
                if display_accounts():
                    print("Here is a list of all your accounts")
                    print('\n')

                    for account in display_accounts():
                        print(f"Account: {account.account_name} | Username: {account.user_name} | Login Email: {account.email} | Loggin password: {account.password}")

                    print('\n')
                else:
                    print('\n')
                    print("You don't seem to have any crdentials for account saved")
                    print('\n')

            elif short_code == 'exit':
                print("Bye.............")
                break
            else:
                print("I really didn't get that. Please use the short codes")    


if __name__ == '__main__':

    main()  
 



