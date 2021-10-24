import unittest #import the unittest module
from user import User #import the User class  from user module

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
        self.assertEqual(len(User.user_list),1
        
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test_User","test@user.com") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)     


if __name__ == '__main__':
    unittest.main()       
