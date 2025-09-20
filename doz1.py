board = [""] * 9
player = "x"
def show():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    
win = [(0, 1, 2),
       (0, 3, 6),
       (0, 4, 8),
       (3, 4, 5),
       (1, 4, 7),
       (2, 5, 8),
       (6, 7, 8),
       (2, 4, 6)]

while True:
    show()
    print(f" نوبت بازیکن  {player}")
    index = int (input("بین خانه ۰ تا ۸ انتخاب کنید : "))
    if board[index] != "":
        print ("این خانه پر است")
        continue
    board[index] = player
    for i , j , k in win :
        if board[j] == board[i] == board[k] != "":
            show()
            print(f"شما برنده شدید!!!{player}")
            exit()
    player= "o" if player == "x" else "x" 
    
show()
print("مساوی")