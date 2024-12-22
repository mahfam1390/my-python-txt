"""def bmm ( a , b ):
    if a > b :
        bmm = b
    elif b > a :
        bmm = a
    while bmm > 1 :
        if a % bmm == 0 and b % bmm == 0 :
            print ( bmm )
            break
        else:
            bmm -= 1
            if a % bmm == 0 and b % bmm == 0 :
                return bmm
def main ():
    x = int ( input ( " enter the first number : "))
    y = int ( input ( " enter the second number : "))
    print(bmm(x,y))
main()
"""
def bmm ( a , b ) :
    if b == 0 :
        return a
    else :
        return bmm ( b , a % b )
def main ():
    x = int ( input ( " enter the first number : "))
    y = int ( input ( " enter the second number : "))
    print(bmm(x,y))
main()