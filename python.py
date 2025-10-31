
def add(a,b):
    return a+b

a = int(input("input the first number: "))
b = int(input("input the second number: "))

result= add(a,b)
print(result)

def multiply(a,b):
    return a*b

def divide(a,b):
    return (a/b)

print("Select an operation to perform:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")   
print("4. Divide")

operation = input()

if operation == '1':
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")
    sum = float(a) + float(b)
    print("The sum is: ", sum)
elif operation == '2':
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")
    difference = float(a) - float(b)
    print("The difference is: ", difference)
elif operation == '3':
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")
    product = float(a) * float(b)
    print("The product is: ", product)
elif operation == '4':
    a = input("Enter the first number: ")
    b = input("Enter the second number: ")
    if float(b) != 0:
        quotient = float(a) / float(b)
        print("The quotient is: ", quotient)
    else:
        print("Error: Division by zero is not allowed.")