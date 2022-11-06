# takes first input
num1 = float(input("Enter first number: "))

# choose operation
print("Operation: +, -, *, /")
select = input("Select operations: ")

#takes second input
num2 = float(input("Enter second number: "))

# check operations and display result
# addition(+) of two numbers
if select == "+":
    print(num1, "+", num2, "=", num1+num2)

# subtraction(-) of two numbers
elif select == "-":
    print(num1, "-", num2, "=", num1-num2)

# multiplication(*) of two numbers
elif select == "*":
    print(num1, "*", num2, "=", num1*num2)

# division(/) of two numbers
elif select == "/":
    print(num1, "/", num2, "=", num1/num2)

else:
    print("Invalid input")