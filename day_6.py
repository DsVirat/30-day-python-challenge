# 🎯 Challenge
# - Generate a random 8-character password

import string
import random

def password_generator():
    all_chars = string.ascii_letters + string.digits + "@!$"
    pw = "".join(random.sample(all_chars,k=8))
    return pw

  # Explanation of the above code :
    # string.ascii_letters : returns a string of all lowercase
    # and uppercase letters i.e. 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # string.digits : returns a string of all digits i.e. '0123456789'
    # all_chars contains all the characters commonly used in strong password
    # random.sample : returns a list of 8 unique random characters from all_chars
    # "".join : joins all the unique characters into a single string

pw = int(input("How many unique passwords do you need : "))
print("Here you go : ")
for i in range(pw):
    print(f"Password {i+1} : {password_generator()}")
    