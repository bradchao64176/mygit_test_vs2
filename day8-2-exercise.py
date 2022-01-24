
#Write your code below this line 
def prime_checker(number):
    is_prime = True
    for n in range(2,number):
        #not self number and divided by other integer
        #質數除了2是偶數, 其他質數一定是奇數
        #質數:大於1,且無法找到除自己本身和1之外的自然數
	    #質數:不能被小於自己的自然數給整除
        if number % n ==0:
            is_prime = False
           

    if is_prime == False:
        print(f"this number is not prime number {number}")
    else:
        print(f"this number is prime number {number}")
    
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
