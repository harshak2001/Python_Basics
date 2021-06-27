#Write a Python program to find factorial of given number (using fact() function)

def factorial(x):
    fact = 1
    for i in range(1,x+1):
        fact = fact * i
    return fact

x = int(input("Enter a positive number:"))
print(f"The factorial of {x} is {factorial(x)}")

