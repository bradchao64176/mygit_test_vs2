#Write yout code below this row

for number in range(1, 101):
    if number %3 == 0 and number %5 == 0:
        print(f"number={number},FizzBuzz")
    elif number % 3 == 0:
        print(f"number={number},Fuzz")
    elif number % 5 == 0:
        print(f"number={number},Buzz")
    else:
        print(number)
