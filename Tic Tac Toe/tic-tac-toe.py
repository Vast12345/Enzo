import time
import json
# Functions for making sure simple inputs are checked
def readNum():
    # A simple function that reads a number, determines if its less than or equal to 9, and then returns the number. It also checks for Value Errors
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
    # A function that will read name of the user who will play as the X in the game. Checks for exceptions and returns the name.
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
    # Same as the function above but is instead for the user who will use O
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



# Menu which will display the three options available for the user
def menu():
    while True:
        try:
            print("\n")
            print("*** TIC TAC TOE ***".center(40))
            print("CHOOSE OPTION".center(40))
            print("\n", "=" * 38, "\n")
            print("1- Play Game")
            print("2- Check Players")
            print("3- Exit\n")
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
            

# Functions that have to do with the list of players as well as the validation of the json file
def bubbleSort(lstWinner):
    # A function that acts as a bubble sort function that reads the time of the time of the users inside the lstWinner list

    n = len(lstWinner)
    for i in range(n):
        for j in range(i+1, n):
            if lstWinner[j][list(lstWinner[j].keys())[0]]["time"] < lstWinner[i][list(lstWinner[i].keys())[0]]["time"]:
                # Swap the elements
                t = lstWinner[j]
                lstWinner[j] = lstWinner[i]
                lstWinner[i] = t


def saveWinner(lstwinner, route):
    try:
        fd = open(route, "w")
    except Exception as e:
        print("Error al abrir el archivo para guardar al empleado.\n", e)
        return None
    try:
        # The below command is what I tried to execute however it failed and I couldn't find a way to sort the json file instead of the physical list
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

    # Go to the function check
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




# Every function used to make sure the tic-tac-toe game works properly. From the board to the win checks, every function here makes sure everything is working smoothly
def gameBoard(board):
    print(" +---+---+---+")
    print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print(" +---+---+---+")
    print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print(" +---+---+---+")
    print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | ")
    print(" +---+---+---+")

def resetBoard():
    global board
    board = ["1", "2", "3",
            "4", "5", "6",
            "7", "8", "9"]

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


# Function for showing the list of winners from those who have the least amount of time.
def showWinners(lstwinners):
    for i in range(len(lstwinners)):
            datos = lstwinners[i]
            key = list(datos.keys())[0]
            print(f"\n")
            print(f"Name: {key}")
            print(f"\n")
            print(f"Time: {lstwinners[i][key]['time']}")
            print(f"\n")
            print(f"Amount of steps: {lstwinners[i][key]['count']}")
            print("\n", "=" * 30, "\n")
            input()



# Variables that are used to display the json file as well as the winners. (Notice how I chose to use the sorting function here instead of inside the saveWinner function)...
routeFile = "Tic Tac Toe/tic-tac-toe.json"
lstWinners = []
lstWinners = loadInfo(lstWinners, routeFile)
bubbleSort(lstWinners)
# print(lstWinners)

winner = None

# The classic while True function that shows the menu, the game, and the list of winners.
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
        showWinners(lstWinners)
    elif op == 3:
        input()
        break