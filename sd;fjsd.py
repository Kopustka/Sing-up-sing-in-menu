
userdata = ['kdjfir832', 'lakj423_R']

def checking_correctness_of_password(word):
    if any(char.isupper() for char in word):
        pass
    else:
        print('должна быть хобы одна заглавная буква')
        return False

    if any(char.isnumeric() for char in word):
        pass
    else:
        print('должна быть хотя бы одна цифра')
        return False

    if any(not char.isalnum() for char in word):
        pass
    else:
        print('должен быть хотя бы один спец-символ')
        return False

    if len(word) < 20 and len(word) > 8:
        pass
    else:
        print('пароль должег быть больше 8 и меньше 20 символов')
        return False

def сhecking_correctness_of_login(word):
    if all(char.isalnum() for char in word):
        pass
    else:
        print('вы логине могут быть только буквы и цифры')
        return False

    if len(word) < 20 and len(word) > 8:
        pass
    else:
        print('логин должег быть больше 8 и меньше 20 символов')
        return False


print(checking_correctness_of_password(userdata[1]))
print(сhecking_correctness_of_login(userdata[0]))
# логин
# не меньше 8
# не больше 20
# только буквы и цифры +

# пароль
# дожна быть заглавная +
# должны быть цифры +
# должен быть спец символ +
# не меньше 8 +
# не больше 20 +


