####################################### SUM OF EVEN NUMBERS ####################################
#even_num = 0
#for i in range(1, 101):
#    if i % 2 == 0:
#        even_num += i
#
#print(f"The sum of all even numbers is: {even_num}")


####################################### FIZZ BUZZ ########################################

for i in range(1, 101):
    if i % 15 == 0:
        print("FIZZ BUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else:
        print(i)