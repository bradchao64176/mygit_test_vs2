

def is_leap(year):
    if year%4==0 and year%100==0 and year%400==0:
        return True
    elif year%4==0 and year%100!=0:
        return True
    else:
        return False

def days_in_month(year, month):
    if not (month > 0 and month < 13):
        return "Your input is invalid!"
    month_days =[31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year) and month==2:
        return 29
    return month_days[month-1]

leap_year = int(input("Please input Year to check leap year. "))
print(f"is leap year? {is_leap(leap_year)}")

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)

print(days)