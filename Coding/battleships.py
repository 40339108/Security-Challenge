import random

ships = {'A':5, 'B':4, 'S':3, 'D':3, 'P':2}
row_l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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
        if ((pos_y + size) <= (len(board) - size + 1)):
            valid = True
            for check_y in range(0, size):
                if (board[pos_y + check_y][pos_x] != ' '):
                    valid = False
            if (valid):
                for y in range(0, size):
                    board[pos_y + y][pos_x] = ship
                placed = True
    else:
        if ((pos_x + size) <= (len(board[0]) - size + 1)):
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
            printBoard(p_board)
            print("Enter Position for {} : ".format(ship), end="")
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

def getMove(c_board, p_board):
    pos = input("Enter Nuke Coordinates: ")
    pos_y = row_l.find(pos[0].upper())
    pos_x = int(pos[1:]) - 1
    if(pos_y >= 0 and pos_y < len(board) and pos_x >= 0 and pos_x < len(board[0])):
        coor = c_board[pos_y][pos_x]
        if(coor = ' '):
                p_board[pos_y][pos_x] = 'M'
        else:
                p_board[pos_y][pos_y] = 'H'

#TODO ADD MOVE HISTORY BOARD

# CREATE BOARDS
p_board = []
c_board = []
initBoard(p_board)
initCompBoard(c_board)

getUserPlacement(p_board)

while(True):
    getMove(c_board)

printBoard(c_board)
