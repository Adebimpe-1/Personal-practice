import random

def generate_password(length=8):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password

length = int(input("Enter password length: "))
print("Generated password:", generate_password(length))
