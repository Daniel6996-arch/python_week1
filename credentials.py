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
      