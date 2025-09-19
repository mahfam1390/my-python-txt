def palindrome ():
    names = input("کلمات خود را وارد کنید : ")
    name_list = names.split()
    name_dict = {}
    for i in name_list:
        if i == i[::-1] :
            name_dict[i] = True
        else:
            name_dict[i] = False
    print(name_dict)
palindrome()