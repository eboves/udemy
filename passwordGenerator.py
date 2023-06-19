import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = [0,1,2,3,4,5,6,7,8,9]
symbols = ['!','"','#','$','%','&','\/',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\/',']','^','_','`','{','|','}','~']

print("Welcome to PassWord Generator")

letter_input = int(input('How many letters would you like to add?\n'))
num_input = int(input('How many numbers would you like to add?\n'))
symbols_input = int(input('How many symbols would you like to add?\n'))

sort_list = []

for letter in range(0, (letter_input)):
    sort_list.append(letters[random.randint(0, len(letters)-1)])

for numb in range(0, (num_input)):
    sort_list.append(num[random.randint(0, len(num)-1)])

for symb in range(0, (symbols_input)):
    sort_list.append(symbols[random.randint(0, len(symbols)-1)])


print(sort_list)