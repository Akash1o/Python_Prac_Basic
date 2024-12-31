try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")
except ValueError as e:
    print("Error: Invalid input, please enter a valid number.")
else:
    print(f"Result: {result}")
finally:
    print("Execution finished.")
