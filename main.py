import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))


total_character = nr_letters + nr_symbols + nr_numbers
password_list = []
password = ""

for x in range(0, nr_letters):
    random_letter = random.randint(0, 51)
    password_list += letters[random_letter]


for y in range(0, nr_numbers):
    random_number = random.randint(0, 9)
    password_list += numbers[random_number]


for z in range(0, nr_symbols):
    random_symbol = random.randint(0, 8)
    password_list += symbols[random_symbol]


for t in range(0, total_character):
    random_character = random.randint(0, len(password_list) - 1)
    password += password_list[random_character]
    password_list.pop(random_character)

print(password)


