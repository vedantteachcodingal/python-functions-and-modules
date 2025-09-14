## function
# question - define a function called my_second_function. this function should print "this is my second function" when called. call this function outside of its definition
# def my_second_function():
#     print("this is my second function")

# my_second_function()


## arguments
# question - define a function that finds the circumference of a circle. The function should take in the radius of the circle as an argument. and then the function should return that circumference value rounded to 2 decimal places
# def circumference(radius):
#     circumference = 2 * 3.14 * radius
#     circumference = round(circumference, 2)
#     return circumference

# print(circumference(5))

## keywords
# question - write a function called check_prime. this function should take in a number as an argument. this function returns True if the number is prime, and returns False otherwise. call this function again and again until a prime number is entered by the user. no need to use recursion here
# def check_prime(num):
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# while True:
#     n = int(input("Enter a prime number: "))
#     if check_prime(n):
#         break
    
## exception handling
# question - read about generic exception handling in google. demonstrate this in next class
try:
    int("abc")
except ValueError:
    print("ValueError")
except Exception as e: # it is best practice to catch specific errors wherever possible, and use generic exception only as a fallback
    print("Oops!:", e)