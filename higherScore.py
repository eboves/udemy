scores = [78, 65, 89, 86, 55, 91, 64, 89, 100]


############################### HIGHER SCORE ###################################
#higher = scores[0]
#
#for score in scores:
#    if score > higher:
#        higher = score
#    
#print(f"The higher score in the list is: {higher}")

############################### HIGHER SCORE ###################################

lowest = scores[0]

for score in scores:
    if score < lowest:
        lowest = score

print(f"The lowest score is: {lowest}")