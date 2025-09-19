def one ():
    one_list = []
    for i in range(10,100):
        number = str(i)
        if number[0] == number[1]:
            one_list.append(int(number))
    print(one_list)

def two ():
    two_list = []
    for i in range(100,1000):
        number = str(i)
        if number[1] == "0":
            two_list.append(int(number))
    print(two_list)

def three ():
    three_list = []
    for i in range(100, 1000):
        if i//100 > i//10%10 + i%100 :
            three_list.append(i)
    print (three_list)
three()
def four ():
    four_list = []
    for i in range (1000, 10000):
        number = str (i)
        if number[0] == number[3] and number[1] == number[2]:
            four_list.append(int(number))
    print(four_list)

four()