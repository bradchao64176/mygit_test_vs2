print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("Can ride")

    age = int(input("please input your age:"))
    if age <12:
        bill = 5
    if age >12 and age <18:
        bill = 7
    if age >18:
        bill = 12

    want_photo = input("Do you want photo? enter Y(es) or N(o):")
    if want_photo =="Y":
        bill +=3
    
    print(f"The total bill is ${bill}")

else:
    print("Can't ride")