import random

ships = {'A':5, 'B':4, 'S':3, 'D':3, 'P':2}
row_l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def startGame():
    p_board = []
    p_guesses = []
    c_board = []
    c_guesses = []

    initBoard(p_guesses)
    initBoard(c_guesses)
    #initBoard(p_board)
    initCompBoard(p_board)
    initCompBoard(c_board)
    printBoard(c_board)
    #getUserPlacement(p_board)

    while(True):
        print("COMP")
        printBoard(c_board)
        print("Computer Score : ", checkPoints(c_guesses))
        print("Player Score : ", checkPoints(p_guesses))
        print("GUESSES")
        printBoard(p_guesses)
        print("YOUR BOARD")
        printBoard(p_board)
        getMove(c_board, p_guesses)
        getCompMove(p_board, c_guesses)


def menu():
    while(True):
        print("BATTLESHITS!")
        print()
        print(" 1) New Game")
        print(" 2) Exit")
        print()
        choice = int(input("> "))
        if (choice == 1):
            startGame()
        elif (choice == 2):
            exit()

def printBoard(board):
    print("     1   2   3   4   5   6   7   8   9   10")
    row = 0
    for y in board:
        print(row_l[row], " | ", end="")
        for x in y:
            print(x, '| ', end="")
        row += 1
        print()

def initBoard(board):
    for y in range(0,10):
        row = []
        for x in range(0,10):
            row.append(' ')
        board.append(row)

def placeShip(board, ship, pos_x, pos_y, dir):
    placed = False
    size = ships.get(ship)
    if (dir == 0):
        if ((pos_y + size) <= len(board)):
            valid = True
            for check_y in range(0, size):
                if (board[pos_y + check_y][pos_x] != ' '):
                    valid = False
            if (valid):
                for y in range(0, size):
                    board[pos_y + y][pos_x] = ship
                placed = True
    else:
        if ((pos_x + size) <= len(board[0])):
            valid = True
            for check_x in range(0, size):
                if (board[pos_y][pos_x + check_x] != ' '):
                    valid = False
            if(valid):
                for x in range(0, size):
                    board[pos_y][pos_x + x] = ship
                placed = True
    return placed

def initCompBoard(board):
    initBoard(board)
    for ship, size in ships.items():
        placed = False
        while(not placed):
            pos_x = random.randint(0, len(board) - 1)
            pos_y = random.randint(0, len(board) - 1)
            dir = random.randint(0, 1)
            placed = placeShip(board, ship, pos_x, pos_y, dir)

def getUserPlacement(board):
    for ship, size in ships.items():
        placed = False
        while(not placed):
            printBoard(board)
            print("Enter Position for {} (size {}): ".format(ship, size), end="")
            pos = input()
            pos_y = row_l.find(pos[0].upper())
            pos_x = int(pos[1:]) - 1
            dir = input("Horizontal (H) or Vertical (V) : ")
            if (dir.upper() == 'H'):
                dir = 1
            elif (dir.upper() == 'V'):
                dir = 0
            else:
                dir = -1
            placed = placeShip(board, ship, pos_x, pos_y, dir)
            if(not placed):
                print()
                print("Wow are you brain dead or something?")
                print()

def checkPoints(board):
    total = 0
    for y in board:
        for x in y:
            if(x == 'H'):
                total += 1
    return total

def getCompMove(p_board, c_guesses):
    move_y = -1
    move_x = -1
    while(True):
        move_y = random.randint(0, len(board))
        move_x = random.randint(0, len(board[0]))
        if(board[y][x] == ' '):
            break
    return len(p_board) * (move_y + 1) + move_x

def getMove(c_board, p_guesses):
    invalidMove = True
    while(invalidMove):
        pos = input("Enter Nuke Coordinates: ")
        pos_y = row_l.find(pos[0].upper())
        pos_x = int(pos[1:]) - 1
        if(pos_y >= 0 and pos_y < len(c_board) and pos_x >= 0 and pos_x < len(c_board[0])):
            coor = c_board[pos_y][pos_x]
            if(coor == ' '):
                    p_guesses[pos_y][pos_x] = 'M'
                    invalidMove = False
            else:
                    p_guesses[pos_y][pos_x] = 'H'
                    invalidMove = False

menu()
