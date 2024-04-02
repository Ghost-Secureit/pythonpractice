import random 
import string 

def generate_password(min_length, num=True, special_char=True):
    letters = string.ascii_letters
    digits = string.digits
    special_char = string.punctuation

    characters = letters
    if num:
        characters += digits
    if special_char:    
        characters += special_char

    pwd = ''
    meets_criteria = False
    has_num = False
    has_spec = False 

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_num = True
        elif new_char in special_char:
            has_spec = True

        meets_criteria = True
        if num:
            meets_criteria = has_num
        if special_char:
            meets_criteria = meets_criteria and has_spec

    return pwd


min_len = int(input('enter the minimum length: '))
has_num = input('do you want to have numbers (y/n)? ').lower() == 'y'
has_spec = input('do you want special characters (y/n)? ').lower() == 'y'
pwd = generate_password(min_len, has_num, has_spec)

print('the generated password is: ', pwd)