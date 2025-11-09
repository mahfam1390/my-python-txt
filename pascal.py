#pascal
def pascal (number):
    t = [1]
    y = [0]
    for i in range (max(number,0)):
        print(t )
        t = [i + j for i , j in zip(t+y , y+t)]
def mane ():
    number = int (input ("please enter your number the line you want:"))
    return pascal(number)
mane()