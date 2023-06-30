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

def calculator():

    num1 = float(input("Please enter the First number: "))

    for operants in operations:
        print(operants)

    keep_calculating = True
    while keep_calculating:

        operation_symbol = input("Select an operation: ")
        num2 = float(input("Please enter the next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continue_calculating = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation. ")
        if continue_calculating == 'y':
            num1 = answer
        else:
            keep_calculating = False
            calculator()
calculator()
#if operation_symbol == "+":
#    func = operations[operation_symbol]
#    answer = func(num1, num2)
#elif operation_symbol == "-":
#    func = operations[operation_symbol]
#    answer = func(num1, num2)
#elif operation_symbol == "*":
#    func = operations[operation_symbol]
#    answer = func(num1, num2)
#elif operation_symbol == "/":
#    func = operations[operation_symbol]
#    answer = func(num1, num2)
#else:
#    print("Please enter a valid Option.")
#    
    