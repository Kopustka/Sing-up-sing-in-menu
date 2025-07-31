from postrges import user_data_login, user_data_reg


User_list = {}

class User:
    def __init__(self, User_name, User_password):
        self.User_name = User_name
        self.User_password = User_password


    @staticmethod
    def logining(User_name, User_password):
        success = user_data_login(User_name, User_password)
        return success


    @staticmethod
    def registration(User_name, User_password):
        user_data_reg(User_name,User_password)
