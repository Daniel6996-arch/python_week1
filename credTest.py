import unittest #import the unittest module
from credentials import Credentials #import the User class  from user module

class TestCreds(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Credentials("Twitter","John-arch","John.arch@email.com","1234567890k") # create user objec
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.account_name,"Twitter")
        self.assertEqual(self.new_account.user_name,"John-arch")
        self.assertEqual(self.new_account.email,"John.arch@email.com")
        self.assertEqual(self.new_account.password,"1234567890k")

                 

if __name__ == '__main__':
    unittest.main()       
