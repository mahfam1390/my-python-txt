score = int(input("نمره را وارد کنید (۰ تا ۲۰): "))

match score:
    case 20:
        print("عالی")
    case 17 | 18 | 19:
        print("خوب")
    case 14 | 15 | 16:
        print("متوسط")
    case 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0:
        print("ضعیف")
    case _:
        print("نمره نامعتبر است.")