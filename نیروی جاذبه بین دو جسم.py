def f (s,k,c) :
	g = 6.693*10 ** (-8)
	i = ((g) * s * k)/(pow(c))
	return i
def pow(c):
	return (c*c)
def main():
	m1 = int (input('number 1 : '))
	m2 = int (input ( ' number 2 : '))
	d  = int ( input (' enter between number 1 and number 2 '))
	print(f(m1, m2, d))
main ()