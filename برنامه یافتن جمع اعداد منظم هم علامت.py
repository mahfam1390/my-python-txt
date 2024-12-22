"""
Hi.
program to find the sum of regular numbers with the same sign.
n1 = number one
n2 = number two
en = end number
far = distance
"""
print (""" Hi. This project is program to find the sum of regular numbers with the same sign.
       please enter the first, second and the end number .
       thanks. """ )
n1 = float(input("enter your first number :"))
n2 = float(input("enter your second number :"))
en = float(input("enter the end number :"))
far = n2 - n1
number = ((en-n1)/far)+1
answer = ((en+n1)/2)*number
if answer == float:
    print (answer)
else :
    print (int(answer))
#print (((en+n1)/2)*number)