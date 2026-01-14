import math
import random

def validateEmail(email):
    is_true = False
    monkeyChar = email.find("@")
    if monkeyChar == -1:
        is_true = False
    else: 
        if email.find(".") > monkeyChar:
            is_true = True

    return is_true

print(validateEmail("asia@example.com"))
print(validateEmail("karol@domena"))
print(validateEmail("user.com"))
