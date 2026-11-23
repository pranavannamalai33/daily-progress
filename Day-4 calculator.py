# Day 4: Simple Calculator

print("Simple Calculator")
a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b == 0:
        print("Error: cannot divide by zero")
    else:
        print("Result:", a / b)
else:
    print("Invalid operator")
