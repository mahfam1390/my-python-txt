#mini library manager
library = 'library-manager.txt'
books = ["فارسی","دفاعی","علوم","قرآن","اجتماعی","عربی","ریاضی"]
def add(books):
    book = input("نام کتاب مورد نظر خود را وارد کنید : ")
    books.append(book)
    return str(books)
def delet(books):
    book = input("نام کتاب مورد نظر خود را وارد کنید : ")
    books.pop(books.index(book))
    return str(books)
def serch(books):
    book = input("نام کتاب مورد نظر خود را وارد کنید : ")
    with open (library, 'w', encoding='utf-8') as printing:
        if book in books:
            printing.write (f"کتاب مورد نظر شما در  خانه {books.index(book)+1} موجود است .")
        else:
            printing.write ("Error 404: Not Found")
def manage(books):
    entery= int(input("""1. افزودن کتاب
                      2. حذف کتاب
                      3.نمایش همه کتاب ها 
                      4. جستجوی کتاب 
                      5. خروج"""))
    with open (library, 'w', encoding='utf-8') as printing:
        
        match entery:
            case 1:
                books = add(books)
                print1 = printing.write(books)
                print("کتاب جدید افزوده شد:")
            case 2 :
                books = delet(books)
                print1 = printing.write(books)
                print(f"کتاب مورد نظر حذف شد. کتابخانه :‌")
            case 3 :  
                print1= printing.write(books)
                print("کتاب ها :",print1)
            case 4 :
                str(serch(books))
            case 5 :
                printing.write ("روز خوبی داشته باشید")
            case _ :
                printing.write ("Error 404: Not Found")
    return books
m = manage(books)
print(m)
