# import the random module
import random

# list of possible characters to use in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator\n")
nr_letters = int(input("How many letters would you like in your password?\n>> "))
nr_symbols = int(input(f"How many symbols would you like?\n>> "))
nr_numbers = int(input(f"How many numbers would you like?\n>> "))

# List to hold randomly selected characters
password_list =[]

# Randomly choose letters, numbers and symbols
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Shuffle the list to make the password more random
random.shuffle(password_list)

# Join the list into a single string
password = ''.join(password_list)

# Print password
print(f"\nYour generated password is: {password}")
