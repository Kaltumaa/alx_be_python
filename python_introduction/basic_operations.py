try:
    # Define two variables
    number1 = 10
    number2 = 5

    # Perform arithmetic operations
    addition = number1 + number2
    subtraction = number1 - number2
    multiplication = number1 * number2
    division = number1 / number2  # Adding division

    # Print the results
    print(f"Addition of {number1} and {number2} is {addition}")
    print(f"Subtraction of {number1} and {number2} is {subtraction}")
    print(f"Multiplication of {number1} and {number2} is {multiplication}")
    print(f"Division of {number1} and {number2} is {division}")  # Print division result

except Exception as e:
    print(f"An error occurred: {e}")
