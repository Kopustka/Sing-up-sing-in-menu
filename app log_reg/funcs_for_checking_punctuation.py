def checking_correctness_of_password(word):
    """
    Validates the password according to the following rules:
    - At least one uppercase letter
    - At least one digit
    - At least one special character (non-alphanumeric)
    - Length between 8 and 20 characters inclusive

    Args:
        word (str): The password string to validate.

    Returns:
        tuple: (bool, str) where bool indicates validity,
               and str contains an error message or empty string if valid.
    """

    if not any(char.isupper() for char in word):
        return False, 'ERROR: Password must contain at least one uppercase letter.'

    if not any(char.isnumeric() for char in word):
        return False, 'ERROR: Password must contain at least one digit.'

    if not any(not char.isalnum() for char in word):
        return False, 'ERROR: Password must contain at least one special character.'

    if not (8 <= len(word) <= 20):
        return False, 'ERROR: Password length must be between 8 and 20 characters.'

    return True, ''


def сhecking_correctness_of_login(word):
    """
    Validates the login according to the following rules:
    - Only letters and digits allowed
    - Length between 8 and 20 characters inclusive

    Args:
        word (str): The login string to validate.

    Returns:
        tuple: (bool, str) where bool indicates validity,
               and str contains an error message or empty string if valid.
    """

    if not word.isalnum():
        return False, 'ERROR: Login may contain only letters and digits.'

    if not (8 <= len(word) <= 20):
        return False, 'ERROR: Login length must be between 8 and 20 characters.'

    return True, ''

