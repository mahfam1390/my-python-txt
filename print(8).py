
def upper_slower(string, upper = 0, lower = 0):
    for i in string :
        if i.isupper():
            upper += 1
        elif i.islower():
            lower +=1
    print (f"biggers :{upper}, lowers : {lower}")

def main():
    string = input ("enter your str :")
    return upper_slower(string)

def sumList ():
    list1 = [1 , 5 , 2]
    print( sum ( list1))

def bigest ():
    list1 = [ 3 , 2, 8, 9 ,3]
    bigger = 0
    for i in list1 :
        if i >= bigger:
            bigger = i
    print(bigger)

def sett () :
    entery = input ("enter your list's items with space :")
    items = entery.split()
    allItems = set(items)
    print (list(allItems))

def count ():
    entery = input ("enter your list :")
    words = entery.split()
    allWords = {}
    for word in words:
        if word in allWords:
            allWords[word] += 1
        else:
            allWords[word] = 1
    print (allWords)

def text ():
    text= input ("enter your str :")
    print (text[::-1])

def strs ():
    text = input("enter your text :")
    print(text[::-1])

def all ():
    text = input ("enter your text :")
    text1 = text.split()
    count = count1 = count2 = count3 = count4 = count5 = 0
    for i in text1 :
        count += 1
    print(f"words : {count}")
    for ch in text:
        count1 += 1
        if ch.isupper():
            count2 += 1
        elif ch.islower():
            count3 += 1
        elif ch.isdigit():
            count4 += 1
        elif ch.isascii():
            count5 += 1
    print (f"letters : {count1}, \n upper letters {count2}, \n lower letters : {count3}, \n numbers : {count4}, \n else : {count5}")



list1 = [1, 5, 3,2]
list1.reverse()
print(list1)

