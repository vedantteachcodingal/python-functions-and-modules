## function
# def my_first_function():
#     print("this is my first function")

# my_first_function()

## arguments
# question - define a function that finds the double of a number. The function should take in the number as an argument. and then the function should return that doubled value.
# def double(x):
#     return x * 2

# answer = double(5)
# print(answer)

## keywords
# activity 1 - write a function called check_prime. this function should take in a number as an argument. this function should return True if the number is prime, and False otherwise
# def check_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# n = int(input("Enter a number: "))
# if check_prime(n):
#     print("It's a prime number")
# else:
#     print("It's not a prime number")
    
# activity 2 - recursive function (function that calls itself until a condition is met (called the base case))
# def countdown(n):
#     if n <= 0:
#         print("Time's up!")
#     else:
#         print(n)
#         countdown(n - 1)

# countdown(5)

# activity 3 - find factorial using recursion (optional)
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1) 

# answer = factorial(5)
# print(answer)

## exception handling
# activity 1 - ask the user to enter their age. if the age is 18 or more, print "You are an adult", otherwise print "You are a minor". if the user enters a non-numeric value, print "Error: Please enter a valid number!"
# try:
#     age = int(input("Enter your age: "))
#     if age >= 18:
#         print("You are an adult")
#     else:
#         print("You are a minor")
# except ValueError:
#     print("Error: Please enter a valid number!")

# activity 2 - this activity is almost the same as activity 1, but here you have to keep asking the user to enter their age until they enter a valid number
while True:
    try:
        age = int(input("Enter your age: "))
        if age >= 18:
            print("You are an adult")
        else:
            print("You are a minor")
        break
    except ValueError:
        print("Error: Please enter a valid number!")

## random and math module

## date, time and calendar module
#         