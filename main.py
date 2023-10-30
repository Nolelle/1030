import calculator

first_number = float(input("Enter in first number: "))
second_number = float(input("Enter in second number: "))

operation = input("Would you like to add/subtract/multiple/divide: ")

if operation == "add":
    result = calculator.add(first_number, second_number)
    print(f"Result: {result}")
elif operation == "subtract":
    result = calculator.subtract(first_number, second_number)
    print(f"Result: {result}")
elif operation == "multiply":
    result = calculator.multiply(first_number, second_number) 
    print(f"Result: {result}")
elif operation == "divide":
    result = calculator.divide(first_number, second_number) 
    print(f"Result: {result}")
else:
    print("Sorry, I do not understand your request.")