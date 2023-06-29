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

num1 = int(input("Please enter the First number: "))

for operants in operations:
    print(operants)

operation_symbol = input("Select an operation")
num2 = int(input("Please enter the next number: "))
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = input("Select another operation: ")
num3 = int(input("Please enter the next number: "))
calculation_function = operations[operation_symbol]
second_answer = calculation_function(num1, num2)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

   
        
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
    