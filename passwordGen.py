import random


def password_generater():
    password_length = 7
    pass_char = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"
    for i in range(password_length):
        pass_key = random.choice(pass_char)
        pass_key=pass_key-password_length

    print(pass_key)


password_generater()
