def readNum():
    while True:
        try:
            num = int(input("Input a tile (1-9) ---> "))
            if num < 1 or num > 9:
                print("Error: Invalid input, must be between 1-9")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return num
        except ValueError:
            print("Error: Invalid input, must be an integer")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")

board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

player = "X"
winner = None
gameRunning = True


def gameBoard(board):
    print(" +---+---+---+")
    print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print(" +---+---+---+")
    print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print(" +---+---+---+")
    print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | ")
    print(" +---+---+---+")

def playerInput(board):
    inp = readNum()
    if board[inp-1].isdigit():
        board[inp-1] = player
    else:
        print("Someone is already in the selected slot.")

def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1].isdigit() == False:
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3].isdigit() == False:
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6].isdigit() == False:
        winner = board[6]
        return True

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0].isdigit() == False:
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1].isdigit() == False:
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2].isdigit() == False:
        winner = board[2]
        return True
    
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0].isdigit() == False:
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2].isdigit() == False:
        winner = board[0]
        return True

def checkTie(board):
    global gameRunning
    is_tie = True  # Assume it's a tie by default

    for element in board:
        if element.isdigit():
            # If any element in the board is still a digit, it's not a tie
            is_tie = False
            break  # No need to check further

    if is_tie:
        gameBoard(board)
        print("TIE")
        gameRunning = False

def switchPlayer():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"

def checkWin():
    global gameRunning
    if checkHorizontal(board) or checkDiagonal(board) or checkVertical(board):
        gameBoard(board)
        print(f"The winner is: {winner}")
        gameRunning = False


while gameRunning:
    gameBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()