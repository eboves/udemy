test_h = int(input("Height of wall: "))
test_w = int(input("width of wall: "))

coverage = 5

def paint_calc(height, width, cover):
    area = height * width
    paint = round(area / cover)
    print(f"You will need {paint} cans of paint.")
    


paint_calc(height=test_h, width=test_w, cover=coverage)
#paint_calc(height=2, width=4, cover=coverage)