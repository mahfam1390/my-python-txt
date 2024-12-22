"""
string = input('enter : ')
print (string.swapcase())
'''
'''
str2 = input ('enter : ')
print (str2.title())
'''
'''
str3 = '\t\   blank'
print (str3.lstrip())
'''
'''
m = input ('enter 1 : ')
m2 = input('enter 2 : ')
for ch in m:
    for i in m2:
        if ch == i :
            print (ch)
"""
'''
'''
n = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']
n2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','V','W','X','Y','Z']
for i in n :
    print (i, str(ord(i)))
for m in n2 :
    print (m, str(ord(m)))