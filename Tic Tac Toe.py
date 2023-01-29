board = [" " for x in range(9)]
def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(symbol):
    if symbol == "X":
        number = 1

    elif symbol == "O":
        number = 2
        
    print("Your turn player {}".format(number))

    while True:
        try:
            choice = int(input("Enter your move (1-9): "))
            if choice not in range(1,10):
                print()
                print("The integer has to be between 1 and 9. Try again")
                continue

            choice -= 1
            if board[choice] != " ":
                print()
                print("That space is already taken. Try again")
                continue

            board[choice] = symbol
            break
        
        except ValueError:
            print()
            print("It has to be an integer. Try again")
        

def is_victory(symbol):
    if (board[0] == symbol and board[1] == symbol and board[2] == symbol) or \
       (board[3] == symbol and board[4] == symbol and board[5] == symbol) or \
       (board[6] == symbol and board[7] == symbol and board[8] == symbol) or \
       (board[0] == symbol and board[3] == symbol and board[6] == symbol) or \
       (board[1] == symbol and board[4] == symbol and board[7] == symbol) or \
       (board[2] == symbol and board[5] == symbol and board[8] == symbol) or \
       (board[0] == symbol and board[4] == symbol and board[8] == symbol) or \
       (board[2] == symbol and board[4] == symbol and board[6] == symbol):
        return True
    
    else:
        return False

def is_draw():
    if " " not in board:
        return True
    
    else:
        return False

while True:
    print_board()
    player_move("X")
    print_board()

    if is_victory("X"):
        print("Player 1 wins! Yippee!")
        break

    elif is_draw():
        print("It's a draw!")
        break

    player_move("O")
    if is_victory("O"):
        print_board()
        print("Player 2 wins! Hooray!")
        break

    elif is_draw():
        print("Draw!")
        break