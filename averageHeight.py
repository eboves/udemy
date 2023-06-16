student_height = [180, 124, 165, 173, 189, 169, 146]
sum_heights = 0
runs = 0

for height in student_height:
    sum_heights += height
    runs += 1

average = round(sum_heights/runs)

print(f"The average hight among the students is {average}")