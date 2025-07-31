# Importing database functions for user login and registration
from postrges import user_data_login, user_data_reg

# Dictionary to store User objects if needed (currently unused)
User_list = {}


class User:
    # Constructor to create a User instance with username and password
    def __init__(self, User_name, User_password):
        self.User_name = User_name
        self.User_password = User_password

    @staticmethod
    def logining(User_name, User_password):
        """
        Static method to check user credentials during login.
        Calls the database function user_data_login which returns True/False.

        Parameters:
            User_name (str): The username entered by the user.
            User_password (str): The password entered by the user.

        Returns:
            bool: True if login successful, False otherwise.
        """
        success = user_data_login(User_name, User_password)
        return success

    @staticmethod
    def registration(User_name, User_password):
        """
        Static method to register a new user.
        Calls the database function user_data_reg to insert user data into DB.

        Parameters:
            User_name (str): The username chosen by the user.
            User_password (str): The password chosen by the user.

        Returns:
            None
        """
        user_data_reg(User_name, User_password)
