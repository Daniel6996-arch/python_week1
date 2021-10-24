class User:
    """
    Class that generates new instances of users.
    """
    user_list = []


    def __init__(self,user_name,password):
        """create arguments for self
        """
        self.user_name = user_name
        self.password = password