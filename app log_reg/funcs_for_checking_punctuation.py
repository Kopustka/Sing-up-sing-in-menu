
def checking_correctness_of_password(word):

    if not any(char.isupper() for char in word):
        return False, 'ОШИБКА: должна быть хотя бы одна заглавная буква'

    if not any(char.isnumeric() for char in word):
        return False, 'ОШИБКА: должна быть хотя бы одна цифра'

    if not any(not char.isalnum() for char in word):
        return False, 'ОШИБКА: должен быть хотя бы один спец-символ'

    if not (8 <= len(word) <= 20):
        return False, 'ОШИБКА: пароль должен быть больше 8 и меньше 20 символов'

    return True, ''


def сhecking_correctness_of_login(word):

    if not word.isalnum():
        return False, 'ОШИБКА: в логине могут быть только буквы и цифры'

    if not (8 <= len(word) <= 20):
        return False, 'ОШИБКА: логин должен быть больше 8 и меньше 20 символов'

    return True, ''
