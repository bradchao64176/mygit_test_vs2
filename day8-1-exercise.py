#Write your code below this line π
import math
def paint_calc(height,width,cover):

    #ceil() η‘ζ’δ»Άι²δ½
    number_of_cans = math.ceil((height * width) / cover)
    return number_of_cans

#Write your code above this line π
# Define a function called paint_calc() so that the code below works.   

# π¨ Don't change the code below π
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
print(f"How many cans of paint you'll need to buy: {paint_calc(height=test_h, width=test_w, cover=coverage)}")