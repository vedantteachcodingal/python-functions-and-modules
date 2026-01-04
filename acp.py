## lesson 1 - function
# question - define a function called my_second_function. this function should print "this is my second function" when called. call this function outside of its definition
# def my_second_function():
#     print("this is my second function")

# my_second_function()


## lesson 2 - arguments
# question - define a function that finds the circumference of a circle. The function should take in the radius of the circle as an argument. and then the function should return that circumference value rounded to 2 decimal places
# def circumference(radius):
#     circumference = 2 * 3.14 * radius
#     circumference = round(circumference, 2)
#     return circumference

# print(circumference(5))

## lesson 3 - keywords
# question 1 - write a function called check_prime. this function should take in a number as an argument. this function returns True if the number is prime, and returns False otherwise. call this function again and again until a prime number is entered by the user. no need to use recursion here
def check_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

while True:
    n = int(input("Enter a prime number: "))
    if check_prime(n):
        break

# question 2 (optional) - take a natural number from user. print the sum of all natural numbers from 1 till the entered natural number. use recursion to find the sum
# def sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum(n - 1) 

# answer = sum(5)
# print(answer)


## lesson 4 - exception handling
# question - read about generic exception handling in google. demonstrate this in next class
# try:
#     int("abc")
# except ValueError:
#     print("ValueError")
# except Exception as e: # it is best practice to catch specific errors wherever possible, and use generic exception only as a fallback
#     print("Oops!:", e)

## lesson 5 - random and math module
# question - use appropriate function from the math module to find the cube root of a given number. use google/chatgpt
# import math
# n = math.cbrt(27)
# print(n)

## lesson 6 - datetime and calendar module
# question 1 - 
import calendar

for month_num in range(1, 13):
    print(calendar.month_name[month_num])


# question 2 - print a random time (HH:SS) within the range from start time (HH:SS) to end time (HH:SS)
# not reviewed
import random
import datetime

start_time = datetime.datetime.strptime("09:00", "%H:%M")
end_time   = datetime.datetime.strptime("10:00", "%H:%M")

total_minutes = int((end_time - start_time).total_seconds() / 60)

random_minutes = random.randint(0, total_minutes)

random_time = start_time + datetime.timedelta(minutes=random_minutes)

print("Random time:", random_time.strftime("%H:%M"))
