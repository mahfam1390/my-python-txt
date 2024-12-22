'''
def charecters (m):
    n = 0
    j = "UOEIAoueia"
    for i in m :
        if i in j:
            n +=1
    return n
s = input ( ' please enter : ')
print ( charecters (s))
'''
'''
def charecter (n):
    d = {}
    k = n.split()
    print ( k )
    for i in k :
        if i in d :
            d[i] += 1
        else :
            d[i] = 1
    return d
s = input( " please enter : ")
print ( charecter ( s ))
'''
'''
def charect (b):
    v = ""
    for ch in range(len(b)) :
        if ch % 2 == 0:
            v = v + b[ch]
    print (v)
s = input (" please enter : ")
charect (s) 
'''
'''
def switch (m):
    d = {1 : 'one', 2 : 'two', 3 : 'three'}
    return d.get(m, 'nothing')
s = int ( input ( " please enter : "))
print ( switch ( s ))
'''