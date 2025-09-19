
inventory_dict = {'برگر': 3, 'پیتزا':5, 'ساندویچ' : 10}
def order ():
    global total_foods
    total_foods = {}
    while True :
        foods_name = input("نام کالا : ")
        if foods_name == "تمام":
            break
        if foods_name in inventory_dict.keys():
            foods = int (input("تعداد کالا : "))   
            total_foods[foods_name]= foods
            if inventory_dict[foods_name] - total_foods[foods_name] >= 0:
                inventory_dict[foods_name] = inventory_dict[foods_name] - foods
                print(f"سفارش شما با موفقست انجام شد. موجودی باقی مانده : {inventory_dict}")
            else:
                print(f"موجودی کافی نیست ! موجودی فعلی  {foods_name} : {inventory_dict[foods_name]} \n سفارش شما : {total_foods} \n موجودی باقی مانده : {inventory_dict}")
        else :
            print("غذای مورد نظر شما در منو موجود نمیباشد. لطفا دوباره امتحان کنید")
order()

print (f"سفارش شما : {total_foods} \n موجودی باقی مانده : {inventory_dict}")