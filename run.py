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
    else:
        print("Wrong password or username")
      
        
    




if __name__ == '__main__':

    main()  
 



