from art import logo
print(logo)

# ADD
def add(n1 , n2):
    return n1 + n2

# SUBTRACT
def subtract(n1 , n2):
    return n1 - n2

# MULTIPLY
def multiply(n1 , n2):
    return n1 * n2

def divide(n1 , n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
     "/" : divide
}

n1 = float(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
should_continue =  True

while should_continue:
    operations_symbol = input("Pick an operation from the line above: ")
    n2 = float(input("What's the next number?: "))
    calculation_function = operations[operations_symbol]
    answer = calculation_function(n1 , n2)

    print(f"{n1} {operations_symbol} {n2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit : ") == "y":
        n1 = answer
    else:
        should_continue = False