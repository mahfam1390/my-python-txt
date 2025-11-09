day = int(input("یک عدد بین ۱ تا ۷ وارد کنید: "))

match day:
    case 1:
        print("شنبه")
    case 2:
        print("یک‌شنبه")
    case 3:
        print("دو‌شنبه")
    case 4:
        print("سه‌شنبه")
    case 5:
        print("چهار‌شنبه")
    case 6:
        print("پنج‌شنبه")
    case 7:
        print("جمعه")
    case _:
        print("عدد نامعتبر است.")