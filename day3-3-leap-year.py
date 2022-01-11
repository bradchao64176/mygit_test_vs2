#  Don't change the code below 
year = int(input("Which year do you want to check? "))
#  Don't change the code above 
#  Write your code below this line 
#  print(year % 4), 取餘數
if year %4 ==0 and year % 100!= 0:
    print(f"this year {year} is Leap year")
elif year % 4 == 0 and year % 100 == 0 and year % 400 ==0:
    print(f"this year {year} is Leap year per 400 years")
else:
    print(f"this year {year} is not Leap year")