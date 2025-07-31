def checking_correctness_of_password(word):
    if any(char.isupper() for char in word):
        pass
    else:
        print('ОШИБКА:должна быть хобы одна заглавная буква')
        return False

    if any(char.isnumeric() for char in word):
        pass
    else:
        print('ОШИБКА:должна быть хотя бы одна цифра')
        return False

    if any(not char.isalnum() for char in word):
        pass
    else:
        print('ОШИБКА:должен быть хотя бы один спец-символ')
        return False

    if len(word) <= 20 and len(word) >= 8:
        pass
    else:
        print('ОШИБКА:пароль должег быть больше 8 и меньше 20 символов')
        return False

    return word



def сhecking_correctness_of_login(word):
    if word.isalnum():
        pass
    else:
        print('ОШИБКА:вы логине могут быть только буквы и цифры')
        return False

    if len(word) <= 20 and len(word) >= 8:
        pass
    else:
        print('ОШИБКА:логин должег быть больше 8 и меньше 20 символов')
        return False

    return word

