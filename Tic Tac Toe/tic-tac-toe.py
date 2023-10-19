import time
import json

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

def readUserX():
    while True:
        try:
            phrase = input("USER X: Input Name --> ")
            phrase = phrase.strip()
            if len(phrase) == 0 or phrase.isalnum() == False:
                print("Error: Invalid input, must be a string")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return phrase
        except Exception as e:
            print(f"Error: Invalid input, must be a string\n{e}")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")

def readUserO():
    while True:
        try:
            phrase = input("USER O: Input Name --> ")
            phrase = phrase.strip()
            if len(phrase) == 0 or phrase.isalnum() == False:
                print("Error: Invalid input, must be a string")
                input("Press any key to continue")
                print("\n", "=" * 30, "\n")
                continue
            return phrase
        except Exception as e:
            print(f"Error: Invalid input, must be a string\n{e}")
            input("Press any key to continue")
            print("\n", "=" * 30, "\n")

def resetBoard():
    global board
    board = ["1", "2", "3",
            "4", "5", "6",
            "7", "8", "9"]




winner = None



def menu():
    while True:
        try:
            print("*** TIC TAC TOE ***".center(40))
            print("CHOOSE OPTION".center(40))
            print("1- Play Game")
            print("2- Check Players")
            print("3- Exit")
            n = int(input("Choose an option (1-3) ---> "))
            if n < 1 or n > 3:
                print("Invalid: Choose between 1-3")
                print("\n", "=" * 30, "\n")
                input()
                continue
            return n
        except ValueError:
            print("Invalid: Input must be an integer between 1-3")
            print("\n", "=" * 30, "\n")
            input()
            
def bubbleSort(lstWinner):
    n = len(lstWinner)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lstWinner[j][list(lstWinner[j].keys())[0]]["time"] > lstWinner[j + 1][list(lstWinner[j + 1].keys())[0]]["time"]:
                # Swap the elements
                t = lstWinner[j]
                lstWinner[j] = lstWinner[j + 1]
                lstWinner[j + 1] = t


def saveWinner(lstwinner, route):
    try:
        fd = open(route, "w")
    except Exception as e:
        print("Error al abrir el archivo para guardar al empleado.\n", e)
        return None
    try:
        # lstwinner = bubbleSort(lstwinner)
        json.dump(lstwinner, fd)
    except Exception as e:
        print("Error al guardar la informacion del emplaeado.\n")
        return None
    
    fd.close()
    return True

def addUser(lstwinners, route, user):
    print("\n\n1. ADD USER")

    time = f"{elapsed_time:.2f}"
    time = float(time)


    dicWinners = {}
    if winner == "X":
        dicWinners[user] = {"time":time, "count":x_count}
        lstwinners.append(dicWinners)
    elif winner == "O":
        dicWinners[user] = {"time":time, "count":o_count}

    if saveWinner(lstwinners, route) == True:
        input("The book has been registered successfully.\nPress any key to continue ... ")
    else:
        input("An error occurred while registering the book.")

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

def checkCount(board):
    global x_count
    global o_count
    x_count = 0
    o_count = 0
    for e in board:
        if e == "X":
            x_count += 1
        elif e == "O":
            o_count += 1
    return print(f"The amount of steps for X is {x_count} and the amount of steps for O is {o_count}\n")

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
        checkCount(board)
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

        checkCount(board)
        gameRunning = False

def loadInfo(lstWinners, route):
    try:
        fd = open(route, "r")
    except Exception as e:
        try:
            fd = open(route, "w")
        except Exception as d:
            print("Error in trying to open archive\n", d)
            return None
    
    try:
        line = fd.readline()
        if line.strip() != "":
            fd.seek(0)
            lstWinners = json.load(fd)
        else:
            lstWinners = []
    except Exception as e:
        print("Error in loading information\n", e)
        return None
    
    # print(lstWinners)
    fd.close()
    return lstWinners






routeFile = "Tic Tac Toe/tic-tac-toe.json"
lstWinners = []
lstWinners = loadInfo(lstWinners, routeFile)
bubbleSort(lstWinners)
print(lstWinners)


while True:
    player = "X"
    gameRunning = True
    op = menu()
    if op == 1:
        userX = readUserX()
        userO = readUserO()
        start_time = time.time()
        resetBoard()
        while gameRunning:
            gameBoard(board)
            playerInput(board)
            checkWin()
            checkTie(board)
            switchPlayer()
        if not gameRunning:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"The amount of time elapsed in playing was {elapsed_time:.2f} seconds.")
            if winner == "X":
                addUser(lstWinners, routeFile, userX)
            elif winner == "O":
                addUser(lstWinners, routeFile, userO)
    elif op == 2:
        pass
    elif op == 3:
        input()
        break