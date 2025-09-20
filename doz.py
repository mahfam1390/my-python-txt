board = [""] * 9
player = "x"
def show():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

for play in range(9):
    show()
    print(f" نوبت بازیکن  {player}")
    index = int (input("بین خانه ۰ تا ۸ انتخاب کنید : "))
    if board[index] != "":
        print ("این خانه پر است")
        continue
    board[index] = player
    if board[0] == board[1] == board[2]!= "":
        show()
        print(f"شما برنده شدید!!!{player}")
        exit()
    if board[0] == board[3] == board[6] != "":
        show()
        print(f"شما برنده شدید!!!{player}")
        exit()
    if board[0] == board[4] == board[8]!= "":
        show()
        print(f"شما برنده شدید!!!{player}")
        exit()
    if board[3] == board[4] == board[5]!= "":
        show()
        print(f"شما برنده شدید!!!{player}")
        exit()
    if board[1] == board[4] == board[7]!= "":
        show()
        print(f"شما برنده شدید!!!{player}")
        exit()
    if board[2] == board[5] == board[8]!= "":
        show()
        print(f"شما برنده شدید!!!{player}")
        exit()
    if board[6] == board[6] == board[8]!= "":
        show()
        print(f"شما برنده شدید!!!{player}")
        exit()
    if board[2] == board[4] == board[6]!= "":
        show()
        print(f"شما برنده شدید!!!{player}")
        exit()
    player= "o" if player == "x" else "x" 
show()
print("مساوی")