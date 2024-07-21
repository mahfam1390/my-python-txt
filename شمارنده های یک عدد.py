#برنامه پيدا کننده شمارنده
r = int ( input ( " Hello, dear user. Welcome to our program. To enter, first enter your favorite number.: "))
# براي دسترسي مدير و يا همان سازنده نيرمزي در نظر ميگيريم
if r == 1390 :
    print (" Welcome manager. ")
else :
    print (" welcome. " )
import math
n = int ( input ( " Please enter your number: " ) )
#ابتدا عدد را ميگيريم
for m in range ( 1,( n+1 ) ):
# و سپس بخش پذير بودن آن براعداد مختلف را آزمايش کرده و اگر بخش پذير بودند پيرينت ميگيريم
    if n%m==0:
        print (m)
for a in range ( 2, n ):
# حال اول يا مرکب بودن آن را مشخص و پرينت ميگيريم
    if n % a == 0:
        print ("This is a composite number.")
        break
else :
    print ("This is the first number.")
# حالا ميبينيم که آيا فرد علاقه اي به ديدن ب.م.م اين عدد را با عدد ديکري دارد يا نه
# اگر داشت مقسوم عليه هاي مشترکرا به او نشان مي دهيم
t = int ( input (  "Do you like b. M. M (greatest common divisor) know this number with another number (1 = yes) (2 = no): "))
if t == 1 :
    p = int ( input (" Enter your second number:"))
    for j in range ( 1,( p+1 ) ):
# و سپس بخش پذير بودن آن براعداد مختلف را آزمايش کرده و اگر بخش پذير بودند پيرينت ميگيريم
        if p%j==0:
            print (j)
    def bmm ( p , n ):
        s = o = 0
        if p>n :
            s = p
        else :
            s = n
        for i in range ( 1 , s+1 ):
            if p % i == 0 and n % i == 0 :
                o = i
                print (" The divisor is the common of these two numbers: " , o )
        return ( o )
    v = bmm ( p , n )
    print ( v )
else :
     print ( " thank you " )
    
# حال نظرسنجي ميکنيم که آيا از کار ما راضي بودند؟
aa = 0
b = 0
c = 0
d = 0
e = 0
a = int ( input (" My satisfaction (1 = excellent) (2 = good) (3 = average) (4 = bad) (5 = very bad): "))
if a == 1 :
    print (" thank you ")
    print ( " Your peers ", ( aa +1 ))
elif a == 2 :
    print ("thank you")
    print ( " Your peers", ( b +1 ))
elif a == 3 :
    print ("thank you")
    print ( " Your peers ", ( c +1 ))
elif a == 4 :
    print ("thank you ")
    print ( " Your peers ", ( d +1 ))
elif a == 5 :
    print ("thank you")
    print ( " Your peers ", ( e +1 ))
else :
    print (" Error: Please use the requested words. The polling time has ended ")
    
    
    
    
