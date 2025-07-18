# Project 1: Calculator

num1 = float(input("Please enter the first digit:"))
num2 = float(input("Please enter the second digit:"))
oper = input("Please enter the operation:")
print("Results:")

if oper == "+":
    print(num1 + num2)
elif oper == "-":
    print(num1 - num2)
elif oper == "*":
    print(num1 * num2)
elif oper == "/":
    print(num1 / num2)
elif oper == "**":  
    print(num1 ** num2)
else:
    print("Invalid Operation!")