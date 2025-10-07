def add(n1, n2):
    return n1+n2
def substract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1/n2

operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide
}

def calculator():
    should_accumulate = True
    input("Welcome to the calculator program!!")
    num1 = float(input("Enter your first number: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above:")  
        num2 = float(input("Enter your second number: "))
        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' tp continue calculating with {answer}, or type 'n' to start a new calculation, or type 'e' to exit: ").lower()
        if choice == 'y':
            num1 = answer
        elif choice == 'n':
            should_accumulate = False
            print("\n"*15)
calculator()



