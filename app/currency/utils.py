import random
import string

# import requests
# import csv
# from faker import Faker


def generate_password(length: int = 10) -> str:

    chars = string.ascii_letters + string.digits
    password = ''

    for _ in range(length):
        password += random.choice(chars)

    return password


def read_txt(name: str = 'requirements.txt') -> str:
    with open(name, "r") as txt_file:
        return txt_file.read()
