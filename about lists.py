"""
first project
about lists
len
"""
l1 = ["ali", "mohammad", "mina"]
l2 = ["mahfam", "grandma"]
#l1 = "Hi!"
#l2 = "hi"
print ("First list length :", len(l1) )
print ("second list length :", len(l2))
"""
second project
max
"""
l3 = ["abc", "a", "amira"]
l4 = [10, 300, 80, 21, 43, 444, 222, 77, 700]
print ("Max value element :", max(l3))
print ("Max value element :", max(l4))
"""
project number 3
min
"""
l5 = [100000, 96345, 986547, 123, 47965, 1234, 777]
l6 = [200000000000, 300000000, 10010101, 234536, 256456, 200, 343456234, 245546]
print ("Min value element :", min (l5))
print ("Min value element :", min (l6))
"""
project number 4
list()
"""
sep = (123, "xyz", "amiri", "obc")
print ("List elements :", list(sep))
"""
project number 5
append
"""
l7 = [4,5]
l8 = [123, 'xyz', 'amiri', 'abs']
l8.append(l7)
print ("Updated list :", l8)
"""
project number 6
count
"""
l9 = ['amiri', 123, 'djhfb',9383048,9384, 123]
print ("count for 123 :", l9.count(123))
print ("count for amiri :", l9.count('amiri'))
"""
project number 7
extend
"""
l10 = [9, 10, 11]
l11 = [1, 2, 3, 4, 5, 6, 7, 8]
l11.extend(l10)
print ("Extended list : ", l11)
"""
8
index
"""
l12 = [947, 'xyz', 'amiri', 123, 'amiri', 'xyz']
print ("Index for xyz :", l12.index('xyz'))
print ("Index for amiri :", l12.index('amiri'))
'''
9
insert
'''
l13 = [123, 'xyz', 'amiri', 'abc']
l13.insert(3, 2009)
print ("Final list :", l13)
"""
10
pop
"""
l14 = [123, 1234, 12345, 'eraa', 'xyz']
l15 = [1234, 12345543, 'gdfh', 'amiri']
print ("a list : ", l14)
"""
11
remove
"""
l16 = [123, ' amiri', 'abc', 'xyz']
print ("List :", l16)
l16.remove('abc')
print ("List :", l16)
"""
12
reverse
"""
l1