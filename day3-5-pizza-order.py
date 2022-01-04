# Don't change the code below 
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L?")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# Don't change the code above 

#Write your code below this line 
bill = 0
if size =="S" or size=="M" or size=="L":
    if size == "S":
        bill = 15
    elif size == "M":
        bill = 20
    elif size == "L":
        bill = 25

    if add_pepperoni == "Y":
        bill_pepperoni = input("Please input S, M or L for Pepperoni, small Pizza +$2, Medium or Large size +$3:")
        if bill_pepperoni == "S":
            bill += 2
        if bill_pepperoni == "M" or bill_pepperoni == "L":
            bill +=3
    
    if extra_cheese == "Y":
        bill +=1

else:
    print("please double check your order Pizza size again.")

print(f"Your final bill is:{bill}")



