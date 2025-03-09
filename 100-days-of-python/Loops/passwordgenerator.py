#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#_________________________MY DUMB CODE_______________________________
# generated_pass = []

# for letter in range(1, nr_letters + 1):
#     rand_letter = random.choice(letters)
#     generated_pass.append(rand_letter)
    
# for symbol in range(1, nr_symbols + 1):
#     rand_symbol = random.choice(symbols)
#     generated_pass.append(rand_symbol)

# for num in range(1, nr_symbols + 1):
#     rand_num = random.choice(numbers)
#     generated_pass.append(rand_num)

# for item in generated_pass:
#     print(item, end="")
#_____________________________________________________________________________

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")

#_________________________DUMB CODE BY ME_________________________________________
# generated_pass = []

# for letter in range(1, nr_letters + 1):
#     rand_letter = random.choice(letters)
#     generated_pass.append(rand_letter)
    
# for symbol in range(1, nr_symbols + 1):
#     rand_symbol = random.choice(symbols)
#     generated_pass.append(rand_symbol)

# for num in range(1, nr_symbols + 1):
#     rand_num = random.choice(numbers)
#     generated_pass.append(rand_num)

# n = len(generated_pass)
# for i in range(n):
#     j = random.randint(0, n - 1)
#     generated_pass[i], generated_pass[j] = generated_pass[j], generated_pass[i]

# for item in generated_pass:
#     print(item, end="")
    
#___________________________________________________________________________________