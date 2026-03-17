from os import system, name as os_name
def clear():
    if os_name == 'nt':
        _ = system('cls')
    else: 
        _ = system('clear')
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        }
while True:
    num1 = eval(input("Enter the first number: "))
    while True:
        operator = input("+\n-\n*\n/\nPick an operator: ").strip()
        num2 = eval(input("Enter the next number: "))
        answer = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")
        new = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").strip()
        if new == "y":
            num1 = answer
        else:
            clear()
            break
