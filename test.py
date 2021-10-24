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


if __name__ == '__main__':
    unittest.main()       
