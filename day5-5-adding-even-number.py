#Instruction
#write a program that caculates the sum of all the even numbers from 1 to 100, including 1 and 100
#eg, 2+4+6+8+10+.....+98+100

# 我的作法
sum=0
for num in range(1,101):
    if num%2==0:
        sum+=num
print(f"Sum={sum}")

#老師的作法
sum=0
for num in range(2,101,2):
    sum+=num
print(f"Sum={sum}")