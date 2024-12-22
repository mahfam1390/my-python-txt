import math
def three (a,b,c):
	p =(a+b+c)/ 2
	f = math.sqrt((p*(p-a)*(p-b)*(p-c)))
	return f
def main ():
	z1= int (input ('ضلع اول : '))
	z2 = int ( input ( ' ضلع دوم : '))
	z3 = int ( input ( ' ضلع سوم : '))
	print(three(z1,z2,z3))
main()