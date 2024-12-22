def bmm ( a , b ):
    m = n = 0
    if a > b :
        m = a
    else : 
        m = b
    for i in range (1 , m + 1):
        if a % i == 0 and b % i == 0 :
            n = i
    return n

def main ():
    x = int ( input ( " enter first number : "))
    y = int ( input ( " enter second number : "))
    print ( bmm (x , y))

main ()