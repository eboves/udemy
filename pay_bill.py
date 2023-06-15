#import random
#names = input('Please enter names separated by comma.')
#names_list = names.split(', ')
#
#rand_number = random.randint(0, len(names_list)-1)
#print(names_list[rand_number])

###################### 4.3 NESTED LISTS ###################

row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

row_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?")

horizontal = int(position[0])-1
vertical = int(position[1])-1

row_map[vertical][horizontal] = "X"

print(f"{row1}\n{row2}\n{row3}")

