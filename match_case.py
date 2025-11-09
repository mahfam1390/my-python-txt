first_number = float(input("عدد اول را وارد کنید: "))
srcond_number = float(input("عدد دوم را وارد کنید: "))
operator = input("عملگر را وارد کنید (+، -، *، /): ")

match operator:

    case '+':
        print("نتیجه:", first_number + srcond_number)
    case '-':
        print("نتیجه:", first_number - srcond_number)
    case '*':
        print("نتیجه:", first_number * srcond_number)
    case '/' :
        if srcond_number != 0:
            print("نتیجه:", first_number / srcond_number)
        else:
            print("خطا: تقسیم بر صفر مجاز نیست.")
    case _:
        print("عملگر نامعتبر است.")
