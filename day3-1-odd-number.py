
mynumber= int(input("Which number do you want to check?"))

if mynumber % 2 ==0:
    print("this is a even number")
    age = int(input("what is your cage?"))
    if age <12:
        print("you shall pay $5")
    elif age <=18:
        print("you shall pay $7")
    else:
        print("you shall pay $12")        
else:
    print("this is a odd number")    
