#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#********Eazy Level - Order not randomised:********
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# ---------------------------------------------------------------------

# # finding letters. "Random.choice()" will help to pick random character and store in total_letters variable.

# for i in range(1,nr_letters+1):
#   total_letters = random.choice(letters)
# #end is one of the parameter of print statement. It stop printing things in new line
#   print(total_letters,end='') 

# # finding numbers

# for i in range(1,nr_numbers+1):
#   total_numbers = random.choice(numbers)
#   print(total_numbers,end='')

# # finding symbols

# for i in range(1,nr_symbols+1):
#   total_symbols = random.choice(symbols)
#   print(total_symbols,end='')
# ---------------------------------------------------------------------


#********Hard Level - Order of characters randomised:********
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# ---------------------------------------------------------------------
final_list = []

for i in range(1,nr_letters+1):
  total_letters = random.choice(letters)
  final_list.append(total_letters)         # Using append function to store characters in a blank list
#print(final_list)                         # for testing purpose

for i in range(1,nr_numbers+1):
  total_numbers = random.choice(numbers)
  final_list.append(total_numbers)         # Using append function to store numbers in a blank list
#print(final_list)                         # for testing purpose

for i in range(1,nr_symbols+1):
  total_symbols = random.choice(symbols)
  final_list.append(total_symbols)         # Using append function to store symbols in a blank list
#print(final_list)                         # for testing purpose

random.shuffle(final_list)                 # Shuffel the list in a random order
#print(final_list)

print("Your Password is: ",end='')
for i in final_list:              # Using "for loop" to go through the list and print the it in a single string.
  a = i
  print(a,end='')

# ---------------------------------------------------------------------

# ********Solution provided by a professor.********

# ---------------------------------------------------------------------
#********Eazy Level********
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)


# ---------------------------------------------------------------------
#********Hard Level********
# password_list = []

# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#   password += char

# print(f"Your password is: {password}")