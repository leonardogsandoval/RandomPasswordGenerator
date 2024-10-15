from random import random
import random

from select import select

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
pass_len=nr_numbers+nr_symbols+nr_letters
#print(pass_len)
groups=[letters,numbers,symbols]

newpass = random.choice(letters)
nr_letters = nr_letters-1
for index in range(2,pass_len+1):

    selection = random.choice(groups)
    if selection == letters:
        nr_letters=nr_letters-1
        newpass = newpass + random.choice(letters)
        if nr_letters == 0:
            groups.remove(letters)

    elif selection== numbers:
        nr_numbers=nr_numbers-1
        newpass = newpass + random.choice(numbers)
        if nr_numbers == 0:
            groups.remove(numbers)


    else:
        newpass = newpass + random.choice(symbols)
        nr_symbols=nr_symbols-1
        if nr_symbols == 0:
            groups.remove(symbols)



print(newpass)