def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "division is not possible."
    else:
        a/b

num1 =int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation =input("Enter the operation you want to process(+.-,*,/):")
if operation =="+":
    print(add(num1,num2))
elif operation =="-":
    print(subtract(num1,num2))
elif operation =="*":
    print(multiply(num1,num2))  
elif operation =="/":
    print(divide(num1,num2))
else:
    print("invalid operation")
        