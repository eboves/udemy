# This is a calculator

#ADD
def add(n1, n2):
    return n1 + n2

#Substract
def substract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

#num1 = int(input("Please enter the First number: "))
#num2 = int(input("Please enter the Second number: "))

for operants in operations:
    print(operants)