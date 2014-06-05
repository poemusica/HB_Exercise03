"""
calculator.py

Take prefix based input and perform appropriate calculations.
"""

def add(tokens):
    num1 = int(tokens[1])
    try:
        num2 = int(tokens[2])
        return num1 + num2
    except:
        return "I don't understand."

def subtract(tokens):
    num1 = int(tokens[1])
    try:
        num2 = int(tokens[2])
        return num1 - num2
    except:
        return "I don't understand."

def multiply(tokens):
    num1 = int(tokens[1])
    try:
        num2 = int(tokens[2])
        return num1 * num2
    except:
        return "I don't understand."

def divide(tokens):
    num1 = float(tokens[1])
    try:
        num2 = int(tokens[2])
        return num1 / num2
    except:
        return "I don't understand."

def mod(tokens):
    num1 = int(tokens[1])
    try:
        num2 = int(tokens[2])
        return num1 % num2
    except:
        return "I don't understand."

def square(tokens):
    # ignore if user entered more than one operand.
    num1 = int(tokens[1])
    return num1 ** 2

def cube(tokens):
    # ignore if user entered more than one operand.
    num1 = int(tokens[1])
    return num1 ** 3

def pow(tokens):
    # ignore if user entered more than one operand.
    num1 = int(tokens[1])
    try:
        num2 = int(tokens[2])
        return num1 ** num2
    except:
        return "I don't understand."

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


        # Test operator and call appropriate function
        if operator == "square":
            print square(tokens)

        if operator == "+":
            print add(tokens)

        if operator == "-":
            print subtract(tokens)

        if operator == "*":
            print multiply(tokens)

        if operator == "/":
            print divide(tokens)

        if operator == "mod":
            print mod(tokens)

        if operator == "cube":
            print cube(tokens)

        if operator == "pow":
            print pow(tokens)



if __name__ == '__main__':
    main()