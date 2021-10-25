class User:
    """
    Class that generates new instances of users.
    """
    user_list = []


    def __init__(self,user_name,password):
        """
        create arguments for self
        """
        self.user_name = user_name
        self.password = password

    def save_user(self):
        """ 
        save_user method saves user objects into user_list
        """
        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self) 
        
    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list        
      

class Credentials:
    """
    Class that generates new instances of credentials.
    """
    accounts_list = []


    def __init__(self,account_name,user_name,email,password):
        """
        create arguments for self
        """
        self.account_name = account_name
        self.user_name = user_name
        self.email = email
        self.password = password
       

    def save_user_account(self):
        """ 
        save_user_credentials method saves user credentials objects into credentials_list
        """
        Credentials.accounts_list.append(self)

    def delete_user_account(self):

        '''
        delete_user_account method deletes a saved account from the accounts_list
        '''

        Credentials.accounts_list.remove(self) 
        
    @classmethod
    def display_accounts(cls):
        '''
        method that returns the accounts list
        '''
        return cls.accounts_list   
            