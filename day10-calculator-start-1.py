
#Calculator

#Add
from soupsieve import select


def add(n1, n2):
    return n1+n2

#Substract
def substract(n1,n2):
    return n1-n2

#Multiply
def multiply(n1,n2):
    return n1*n2

#Divide
def divide(n1,n2):
    return n1/n2

#function to be an object value
operations = {
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide
}

#Iterate operation
for oper in operations:
    print(oper)
    print(operations[oper])

def calculator(operation_symbol,num1,num2):
    operation_symbol = input("Pick an operation from the line above:")
    calculate_function = operations[operation_symbol]
    answer = calculate_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

'''
operation_symbol = input("Pick an operation from the line above:")
calculate_function = operations[operation_symbol]
first_answer = calculate_function(num1,num2)
print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = input("Pick an operation from the line above:")
calculate_function = operations[operation_symbol]
num3 = int(input("what's the third number? "))
second_answer = calculate_function(first_answer,num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

'''   

stop_caculate = False
while not stop_caculate:
    operation_symbol = input("Pick an operation from the line above:")
    if operation_symbol not in operations:
        print(f"{operation_symbol} is invalid symbol, please input operation symbol again")
    else:
        num1 = int(input("what's the first number? "))
        num2 = int(input("what's the second number? "))
        calculate_function = operations[operation_symbol]
        answer = calculate_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        #to determine is going to be continue calculated or stop
        calculate_again = input("Continue calculate, type Y(es), otherwise, type N(ot)")
        if calculate_again.lower() == "n" or calculate_again.lower() == "not":
            stop_caculate = True
