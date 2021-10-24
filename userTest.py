import unittest #import the unittest module
from user import User #import the User class  from user module
from user import Credentials #import the Credentials class  from credentials module

class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Daniel","123456kky") # create user objec
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Daniel")
        self.assertEqual(self.new_user.password,"123456kky")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []    

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test_User","test@user.com") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Test_User","test@user.com") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_list),1) 

    def test_display_users(self):
            '''
            method that returns a list of all users saved
            '''

            self.assertEqual(User.display_users(),User.user_list)   




class TestCreds(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Credentials("Twitter","John-arch","john.arch@email.com","1234567890k") # create account object
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.account_name,"Twitter")
        self.assertEqual(self.new_account.user_name,"John-arch")
        self.assertEqual(self.new_account.email,"john.arch@email.com")
        self.assertEqual(self.new_account.password,"1234567890k")

    def test_save_user_account(self):
        '''
        test_save_user_account test case to test if the account object is saved into
        the accounts list
        '''
        self.new_account.save_user_account()
        self.assertEqual(len(Credentials.accounts_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.accounts_list = []    

    def test_save_multiple_user_accounts(self):
            '''
            test_save_multiple_user_accounts to check if we can save multiple user accounts
            objects to our accounts_list
            '''
            self.new_account.save_user_account()
            test_account = Credentials("Twit","Ian-arc","john.arch@email.com","1234567890k") # new user_account
            test_account.save_user_account()
            self.assertEqual(len(Credentials.accounts_list),2)

    def test_delete_user_account(self):
            '''
            test_delete_user_account to test if we can remove an account from our account list
            '''
            self.new_account.save_user_account()
            test_account = Credentials("Twit","Ian-arc","john.arch@email.com","1234567890k") # new user_account
            test_account.save_user_account()

            self.new_account.delete_user_account()# Deleting a user_account object
            self.assertEqual(len(Credentials.accounts_list),1) 

    def test_display_accounts(self):
            '''
            method that returns a list of all accounts saved
            '''

            self.assertEqual(Credentials.display_accounts(),Credentials.accounts_list)


if __name__ == '__main__':
    unittest.main()       


if __name__ == '__main__':
    unittest.main()       
