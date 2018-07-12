import random
import socket
import os

ships = {'A':5, 'B':4, 'S':3, 'D':3, 'P':2}
row_l = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def singlePlayer():
    p_board = []
    p_guesses = []
    c_board = []
    c_guesses = []

    initBoard(p_guesses)
    initBoard(c_guesses)
    initCompBoard(c_board)

    place_ships = input("Automatically Place Ships (Y / N) : ")
    if(place_ships[0] == 'Y' or place_ships[0] == 'y'):
        initCompBoard(p_board)
    else:
        getUserPlacement(p_board)

    target = 0
    for ship, size in ships.items():
        target += size

    while(True):
        c_points = checkPoints(c_guesses)
        p_points = checkPoints(p_guesses)
        print("Computer Score : ", c_points)
        print("Player Score : ", p_points)
        if(c_points == target):
            print("Computer Won!")
            break
        elif(p_points == target):
            print("Player Won!")
            break
        print("YOUR GUESSES")
        printBoard(p_guesses)
        print("YOUR BOARD")
        printBoard(p_board)
        getMove(c_board, p_guesses)
        getCompMove(p_board, c_guesses)

# H = HELLO ; 0 = first ; 1 = second
# V = VALID ; 0 = invalid ; 1 = valid
# E = END ;

def host():
    port = 4444
    ip = input("Enter your IP Address: ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.bind(server_address)
    sock.listen(1)
    print("Server IP :", ip + ":" + str(port))
    print("Waiting for player...")
    connection, client_address = sock.accept()
    print("Player joined!")
    h_board = []
    h_guesses = []
    c_board = []
    c_guesses = []

    initBoard(h_guesses)
    initBoard(c_guesses)
    initCompBoard(h_board)
    initCompBoard(c_board)

    # first = random.randint(0, 1)
    # if(first):
    #     getMove(p)
    # else:
    while(True):
        try:
            data = connection.recv(16)
            print(bytes.decode(data, 'UTF-8'))
            #if(tryMove(bytes.decode(data, 'UTF-8')))
        finally:
            connection.close()

def checkResponse(response):
    #CODE
    print(response)

def join():
    response = ''
    port = 4444
    ip = input("Enter the IP Address of the host: ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, port)
    sock.connect(server_address)
    print("Joined server!")
    while (True):
        data = sock.recv(16)
        response = bytes.decode(data, 'UTF-8')
        check = checkResponse(repsonse)

def local():
    p1_board = []
    p1_guesses = []
    p2_board = []
    p2_guesses = []

    initBoard(p1_guesses)
    initBoard(p2_guesses)

    print("PLAYER ONE!")
    place_ships = input("Automatically Place Ships (Y / N) : ")
    if(place_ships[0] == 'Y' or place_ships[0] == 'y'):
        initCompBoard(p1_board)
    else:
        getUserPlacement(p1_board)
    os.system("clear")

    print("PLAYER TWO!")
    place_ships = input("Automatically Place Ships (Y / N) : ")
    if(place_ships[0] == 'Y' or place_ships[0] == 'y'):
        initCompBoard(p2_board)
    else:
        getUserPlacement(p2_board)
    os.system("clear")

    target = 0
    for ship, size in ships.items():
        target += size

    while(True):
        p1_points = checkPoints(p1_guesses)
        p2_points = checkPoints(p2_guesses)
        print("Player 1 Score : ", p1_points)
        print("Player 2 Score : ", p2_points)
        if(p1_points == target):
            print("Player One Won!")
            break
        elif(p2_points == target):
            print("Player Two Won!")
            break

        input("Player one ready?")
        print("PLAYER ONE!")
        print("GUESSES")
        printBoard(p1_guesses)
        print("BOARD")
        printBoard(p1_board)
        getMove(p2_board, p1_guesses)
        printBoard(p1_guesses)
        input("Player two's turn!")
        os.system("clear")

        p1_points = checkPoints(p1_guesses)
        p2_points = checkPoints(p2_guesses)
        print("Player 1 Score : ", p1_points)
        print("Player 2 Score : ", p2_points)
        if(p1_points == target):
            print("Player One Won!")
            break
        elif(p2_points == target):
            print("Player Two Won!")
            break

        input("Player two ready? ")
        print("PLAYER TWO!")
        print("GUESSES")
        printBoard(p2_guesses)
        print("BOARD")
        printBoard(p2_board)
        getMove(p1_board, p2_guesses)
        printBoard(p2_guesses)
        input("Player ones's turn!")
        os.system("clear")

def multiplayer():
    while(True):
        print()
        print(" 1) Join")
        print(" 2) Host")
        print(" 3) Local")
        print()
        choice = int(input("> "))
        if(choice == 1):
            join()
        elif(choice == 2):
            host()
        elif(choice == 3):
            local()

def menu():
    while(True):
        print("BATTLESHITS!")
        print()
        print(" 1) Single Player")
        print(" 2) Multiplayer")
        print(" 3) Quit")
        print()
        choice = int(input("> "))
        if (choice == 1):
            singlePlayer()
        elif (choice == 2):
            multiplayer()
        elif (choice == 3):
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
    initBoard(board)
    for ship, size in ships.items():
        placed = False
        while(not placed):
            printBoard(board)
            print("Enter Position for {} (size {}) : ".format(ship, size), end="")
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

def tryMove(board, guesses, pos_y, pos_x):
    if(guesses[pos_y][pos_x] == ' '):
        if (board[pos_y][pos_x] == ' '):
            guesses[pos_y][pos_x] = 'M'
            board[pos_y][pos_x] = 'M'
            return True
        else:
            guesses[pos_y][pos_x] = 'H'
            board[pos_y][pos_x] = 'H'
            return True

def getCompMove(p_board, c_guesses):
    while(True):
        pos_y = random.randint(0, len(p_board) - 1)
        pos_x = random.randint(0, len(p_board[0]) - 1)
        if(tryMove(p_board, c_guesses, pos_y, pos_x)):
            break

def getMove(c_board, p_guesses):
    while(True):
        pos = input("Enter Nuke Coordinates : ")
        if(len(pos) > 1 and len(pos) < 4):
            pos_y = row_l.find(pos[0].upper())
            pos_x = int(pos[1:]) - 1
            if(pos_y >= 0 and pos_y < len(c_board) and pos_x >= 0 and pos_x < len(c_board[0])):
                if(tryMove(c_board, p_guesses, pos_y, pos_x)):
                    break

menu()
