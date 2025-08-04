# Basic Calculator Program
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sign = input("Enter the sign of operation (+, -, *, /): ")

if sign == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif sign == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif sign == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif sign == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid sign. Please enter one of +, -, *, /.")
