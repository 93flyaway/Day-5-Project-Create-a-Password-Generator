#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# randomly choose and concatenate onto a password variable in order the specified number of letters, symbols, and numbers in loops.
password = ""
for letter in range(0, nr_letters):
  password = password + random.choice(letters)
for symbol in range(0, nr_symbols):
  password = password + random.choice(symbols)
for number in range(0, nr_numbers):
  password = password + random.choice(numbers)

print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#typecast non-randomized password into a list
password_components = list(password)

#put together a new list of index numbers for the non-randomized password list.
index = []
for i in range(0, len(password)):
  index.append(i)

print("---------------------------")

# set new password variable equal to empty string
new_password = ""

# for the length of the password, repeat:
#choose a random element from the index number list.
#pick out the element at the chosen index number from the password list using the pop() method, and concatenate to the new password variable.
#remove the last element in the index list.
for i in range(0, len(password)):
  random_index = random.choice(index)
  new_password = new_password + password_components.pop(random_index)
  index.pop(-1)

#print password with randomized order
print(new_password)