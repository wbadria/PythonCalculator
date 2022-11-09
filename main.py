# This is a simple calculator that takes integer or decimal numbers and performs some simple calculations as required.
# A good feature in this calculator is its ability to perform calculations using signs as input (e.g. +, *, /, etc..) or
# words instead (e.g. plus, multiplied by, modulus, etc..)
# For example: the user can enter (5 + 3) or (5 plus 3). And the output will be identical for both cases: 5 + 3 = 8


def input_process(equation):
    """Separates numbers from text. Returns two numbers and an operator"""
    # Removes spaces from the input and stores it in the join_string
    joined_string = "%s" % ("".join(equation.split(" ")))
    new_string = ""
    num1 = ""
    op = ""
    num2 = ""
    # Finds the first number whether an integer or decimal
    for char in joined_string:
        if char.isdigit() or char == ".":
            num1 += char
        else:
            # Break when facing anything other than a number or a dot "."
            # and store the rest in the variable new_string after removing num1 from joined_string
            new_string = joined_string.removeprefix(num1)
            break
    # This loop will search within new_string to find the second number
    for char in new_string:
        if char.isdigit() or char == ".":
            num2 += char
        # Values other than numbers and ".", will be the operation
        else:
            op += char
    return num1, op, num2


def calculation(first_num, operator, second_num):
    """Validates the operators and returns the result of the calculation"""
    if operator == "+" or operator == "plus":
        sign = "+"
        result = first_num + second_num
        return result, sign
    elif operator == "-" or operator == "minus":
        sign = "-"
        result = first_num - second_num
        return result, sign
    elif operator == "*" or operator == "x" or operator == "multipliedby":
        sign = "*"
        result = first_num * second_num
        return result, sign
    elif operator == "/" or operator == "dividedby":
        sign = "/"
        result = first_num / second_num
        return result, sign
    elif operator == "%" or operator == "modulus":
        sign = "%"
        result = first_num % second_num
        return result, sign
    else:
        # In case of a wrong entry or the operation is no supported, the program will be restarted.
        print("Invalid operator!\n")
        calculator()


def calculator():
    """Runs calculations on integer and floating point equations"""
    calculator_is_on = True
    while calculator_is_on:
        user_input = input("1) Author info\n2) Integer Operation\n"
                           "3) Floating point Operation\n0) Exit\nSelect an option (0, 1, 2, or 3): ")
        # when user chooses 1, display my information
        if user_input == "1":
            print("Name: Wael Badria\n")
        # when press 2, take do integer calculation
        elif user_input == "2":
            # make all the entries lower case for better functionality.
            int_equation = input("Enter an integer equation: ").lower()
            # pass the user_input to input_process to separate numbers from the operator
            final_equation = input_process(int_equation)
            # make sure the numbers entered are integers to continue, otherwise ask the user for a valid entry
            char1 = final_equation[0]
            char2 = final_equation[2]
            if char1.isdigit() and char2.isdigit():
                first_number = int(final_equation[0])
                operator = final_equation[1]
                second_number = int(final_equation[2])
                # pass the numbers and operator to calculation function
                final_result = calculation(first_number, operator, second_number)
                # in case of division, we need the results to be in 2 decimal
                result = final_result[0]
                sign = final_result[1]
                if sign == "/":
                    result = '%.2f' % result
                print(f"OUTPUT: {first_number} {sign} {second_number} = {result}\n")
            else:
                print("Invalid entry! Enter integers only.\n")
        elif user_input == "3":
            flt_equation = input("Enter a floating equation: ").lower()
            final_equation = input_process(flt_equation)
            op_char = final_equation[1]
            # exclude the modulus operator since it is not allowed with floating point equations
            if op_char != "%" and op_char != "modulus":
                first_number = float(final_equation[0])
                operator = final_equation[1]
                second_number = float(final_equation[2])
                final_result = calculation(first_number, operator, second_number)
                result = final_result[0]
                sign = final_result[1]
                print(f"OUTPUT: {first_number} {sign} {second_number} = {'%.2f' % result}\n")
            else:
                print("Invalid operator for floating calculation!\n")
        # Terminates the calculator when user enters 0
        elif user_input == "0":
            calculator_is_on = False
        # When user enters wrong entry, the program will start over
        else:
            print("Invalid selection! Try again.\n")


# Start the calculator
calculator()
