
menu = {"همبرگر ذغالی" : 153000,
         "چیز برگر ذغالی ": 163000 ,
         "دوبل برگر آقای خرچنگ" : 250000,
         "همبرگر ویژه بابسفنجی": 300000,
         "پیتزا پاتریک" : 250000,
         "پیتزا مخصوص": 210000,
         "پیتزا مخلوط": 205000,
         "پیتزا پپرونی": 225000,
         "فیله مرغ گریل شده":160000,
         "هات داگ پاتریک": 190000,
         "کوکتل تنوری اختاپوس": 140000,
         "بندری": 140000,             
         "فیله سوخاری": 255000,
             "قارچ سوخاری": 120000,
             "سیب زمینی": 100000,
             "سیب زمینی ویژه بابسفنجی":155000,
             "سالاد فصل": 50000,
             "سالاد اندونزی": 70000}

print(f""" با سلام. به رستوران بابسفنجی و دوستان خوش آمدید 
      منو : {menu.keys()}
          """)
def food () :
    global food_name
    global number
    global order
    global price
    order = {}
    while True :
        food_name = input("نام غدای مورد نظر خود را وارد کنید :")
        if food_name == "تمام":
            break
        if food_name in menu.keys():
            number = int(input ("تعداد غذای مورد نظر خود را وارد کنید : "))
            price = menu[food_name]
            order[food_name] = order.get(food_name, 0) + number
        else :
            print("غذای مورد نظر شما در منو موجود نمیباشد. لطفا دوباره امتحان کنید")
    return order
def total_price (order):
    total = 0
    for i , j in order.items ():
        total+= menu[i] * j
    return total
order = food()
total = total_price (order)
print(f"  سفارشات : {order} ", f"  قیمت کل : {total}" )