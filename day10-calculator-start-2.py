
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

def calculator():
    num1 = int(input("what's the first number? "))
    continue_calculate = True
    while continue_calculate:
        operation_symbol = input("Pick an operation from the line above:")
        num2 = int(input("what's the next number? "))
        calculate_function = operations[operation_symbol]
        answer = calculate_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculateion:: ")=="y":
            num1=answer
        else:
            continue_calculate = False
            calculator()

calculator()
