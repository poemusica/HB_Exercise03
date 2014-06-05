"""
calculator.py

Take prefix based input and perform appropriate calculations.
"""

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def square(num1):
    return num1 ** 2

def cube(num1):
    return num1 ** 3

def power(num1, num2):
    return num1 ** num2

def mod(num1, num2):
    return num1 % num2

def main():
    # List of operators that this program accepts.
    valid_operators = [
        "+", 
        "-", 
        "*", 
        "/",
        "square",
        "cube",
        "pow",
        "mod"
    ]
   
    while True:
        # Get calculation to perform from user
        user_input = raw_input("> ").lower()
        
        # End script if user enters q
        if user_input == "q":
            break

        # Split user input into operator and operands
        tokens = user_input.split()

        # Tests number of tokens. This program requires 2 or 3 only.
        if len(tokens) < 2 or len(tokens) > 3:
            print "I don't understand."
            continue

        operator = tokens[0]

        # Confirm valid prefix syntax
        if tokens[0] not in valid_operators:
            print "I don't understand."
            continue

        num1 = float(tokens[1])
        if len(tokens) > 2:
              num2 = float(tokens[2])
        else:
            # set empty num2 to 1 to prevent divide by zero error
            num2 = 1


        # Test operator and call appropriate function
        if operator == "square":
            print square(num1, num2)

        if operator == "+":
            print add(num1, num2)

        if operator == "-":
            print subtract(num1, num2)

        if operator == "*":
            print multiply(num1, num2)

        if operator == "/":
            print divide(num1, num2)

        if operator == "mod":
            print mod(num1, num2)

        if operator == "cube":
            print cube(num1, num2)

        if operator == "pow":
            print pow(num1, num2)



if __name__ == '__main__':
    main()