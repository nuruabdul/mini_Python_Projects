# Tech with Tim
#  python3 .\password_generator.py or  python .\password_generator.py to run the code.

import numbers
import random
import string

def generate_password(min_length, numbers=True,special_characters=True):
    # pass
     letters = string.ascii_letters
     digits = string.digits
     special = string.punctuation

     characters = letters
     if numbers:
        characters += digits
     if special_characters:
       characters += special

     pwd = ""
     meets_criteria = False
     has_number = False
     has_special = False

     while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
           has_number = True
        elif new_char in special:
           has_special = True

        meets_criteria = True
        if numbers:
           meets_criteria = has_number
        if special_characters:
           meets_criteria = meets_criteria and has_special

     return pwd
min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y" 
has_special = input("Do you want to have special characters(y/n)? ") .lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)

# sample Passwords generated are as follows:-
#1. )I)%[~s,=+O1
#2. u>:Hb;c%6I
#3. )AW/^,!c_Zyhgy9


 

# print("hello World")
# generate_password(10, False,False)