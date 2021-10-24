class Credentials:
    """
    Class that generates new instances of credentials.
    """
    credentials_list = []


    def __init__(self,account_name,user_name,email,password):
        """
        create arguments for self
        """
        self.account_name = user_name
        self.user_name = user_name
        self.email = email
        self.password = password
       

    def save_user_credentials(self):
        """ 
        save_user_credentials method saves user credentials objects into credentials_list
        """
        Credentials.credentials_list.append(self)

    def delete_user_credentials(self):

        '''
        delete_user_credentials method deletes a saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self) 
        
    @classmethod
    def display_all_accounts(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list   
      