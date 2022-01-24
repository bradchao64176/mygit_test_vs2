#Write your code below this line 👇
import math
def paint_calc(height,width,cover):

    #ceil() 無條件進位
    number_of_cans = math.ceil((height * width) / cover)
    return number_of_cans

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
print(f"How many cans of paint you'll need to buy: {paint_calc(height=test_h, width=test_w, cover=coverage)}")