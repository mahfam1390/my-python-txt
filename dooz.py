safhe = [""] * 9
player = "x"
def show():
    print(safhe[0], "|", safhe[1], "|", safhe[2])
    print("--+---+--")
    print(safhe[3], "|", safhe[4], "|", safhe[5])
    print("--+---+--")
    print(safhe[6], "|", safhe[7], "|", safhe[8])
    
win = [(0, 1, 2),
       (0, 3, 6),
       (0, 4, 8),
       (3, 4, 5),
       (1, 4, 7),
       (2, 5, 8),
       (6, 7, 8),
       (2, 4, 6)]

for play in range (9):
    show()
    print(f" نوبت بازیکن  {player}")
    index = int (input("بین خانه ۰ تا ۸ انتخاب کنید : "))
    if safhe[index] != "":
        print ("این خانه پر است")
        continue
    safhe[index] = player
    for i , j , k in win :
        if safhe[j] == safhe[i] == safhe[k] != "":
            show()
            print(f"شما برنده شدید!!!{player}")
            exit()
#    player= "o" if player == "x" else "x"
    if player == "x" :
        player = "o"
    else:
        player= "x"

show()
print("مساوی")
