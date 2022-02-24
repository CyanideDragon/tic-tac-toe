print("haha python go b" + "r" * 8)

PLAYER1 = "X"
PLAYER2 = "O"

def main():
    board = [[" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]]
    
    current_player = PLAYER1

    winConCheck = False
    loopCount = 0

    while True:
        prnt_board(board)
        print(f"Player {current_player}, it is your turn.")
        y_coordinate = int(input("which column do you wish to play in?")) - 1
        x_coordinate = int(input("which row do you wish to play in?")) - 1

        if (y_coordinate < 3 or y_coordinate >= 1) and (x_coordinate < 3 or x_coordinate >= 1):
            if board[x_coordinate][y_coordinate] == " ":
                board[x_coordinate][y_coordinate] = current_player
                winConCheck = winCon(board)
                loopCount += 1
                if winConCheck == True:
                    prnt_board(board)
                    print(f"Congratulations! player {current_player} Wins!")
                    break
                if current_player == "X":
                    current_player = PLAYER2
                elif current_player == "O":
                    current_player = PLAYER1
                if loopCount == 9:
                    prnt_board(board)
                    print ("Tie! It's a cat's game!")
                    break
            else:
                print("That spot has been played in already!")
        else:
            print("That location does not exist.")

def prnt_board(board):
    for item in board:
        print(item)

def winCon(board):
    if (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O") or (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") or (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O") or (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") or (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O") or (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") or (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O") or (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X") or (board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O") or (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X") or (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O") or (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X") or (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):
        return True
    else:
        return False

if __name__ == "__main__":
    main()