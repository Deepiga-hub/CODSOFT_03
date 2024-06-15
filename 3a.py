'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Welcome to Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Length must be a positive integer.")
                continue
            password = generate_password(length)
            print("Generated Password:", password)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer length.")

if __name__ == "__main__":
    password_generator()


