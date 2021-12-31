# Don't change the code below 
# age = input("What is your current age?")
# Don't change the code above 
#Write your code below this line 

age = input("What is your current age?")
years_remaining = 70 - int(age)
day_remaining = years_remaining *365
week_remaining = years_remaining  * 52
month_remaining = years_remaining * 12

message = f"You have {day_remaining} days, {week_remaining} weeks, {month_remaining} months left "
print(message)




