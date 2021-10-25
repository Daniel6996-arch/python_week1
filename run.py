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
 



