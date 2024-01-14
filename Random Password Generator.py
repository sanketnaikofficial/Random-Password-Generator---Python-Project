import random
import string

def generate_password(length=12):
    # Defining the character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combining all the character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensuring atleast one character from each set
    password = random.choice(uppercase_letters) + random.choice(lowercase_letters) + random.choice(digits) + random.choice(special_characters)

    # randomaization of the characters
    password += ''.join(random.choice(all_characters) for _ in range(length - 4))

    # Shuffling the password to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    final_password = ''.join(password_list)

    return final_password
random_password = generate_password()
print("Random Password:", random_password)    

