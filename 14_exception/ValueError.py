def add_numbers():
    try:

        num1 = int(input("Enter the first number: "))  # Convert input to integer
        num2 = int(input("Enter the second number: "))  # Convert input to integer
        # Add num1 and num2
        result = num1 + num2
        # Show the ouput of sum two number
        print(f"The sum of {num1} and {num2} is {result}.")
        # check vaues are int or not 
    except ValueError:
        print("Plese Enter Valid")

add_numbers()