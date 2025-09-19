from math import *
number = int(input("enter your num ber : "))
def factorial_with_for(number):
    one = 1
    for i in range (1, number +1):
        one = one * i
        print(i,end=" ")
    print (one)
def factorial_function(number):
    if number == 0:
        return 1
    else:
        return number * factorial_function(number-1)
factorial_with_for(number)
print(factorial_function(number)) 
print(factorial(number))