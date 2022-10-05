'''
Autor:Edgar Francisco Hernández Méndez 
Fecha:04/10/22
Actividad:gato
'''



print("Desafia a la computadora:")
print()
from random import randrange

def DisplayBoard(board):
    print("+-------" * 3,"+",sep="")
    for row in range(3):
        print("|       " * 3,"|",sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ",end="")
        print("|")
        print("|       " * 3,"|",sep="")
        print("+-------" * 3,"+",sep="")

def EnterMove(board):
    ok = False  
    while not ok:
        move = input("introduce tu movimiento: ") 
        ok = len(move) == 1 and move >= '1' and move <= '9' 
        if not ok:
            print("Lugar erroneo  - intenta otra vez") 
            continue
        move = int(move) - 1    
        row = move // 3     #The rows
        col = move % 3      # The columns
        sign = board[row][col]  
        ok = sign not in ['O','X'] 
        if not ok:  
            print("Intenta otra vez!")
            continue
    board[row][col] = 'O' 

def MakeListOfFreeFields(board):
    free = []   #  empty list
    for row in range(3): # range for rows
        for col in range(3): # range for columns
            if board[row][col] not in ['O','X']: 
                free.append((row,col)) # new tuple added 
    return free


def VictoryFor(board,sgn):
    if sgn == "X":  
        who = 'Yo'  
    elif sgn == "O":
        who = 'Tu'
    else:
        who = None  
    cross1 = cross2 = True  #
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn: 
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
            return who
        if board[rc][rc] != sgn: 
            cross1 = False
        if board[2 - rc][2 - rc] != sgn: 
            cross2 = False
    if cross1 or cross2:
        return who
    return None

def DrawMove(board):
    free = MakeListOfFreeFields(board)
    tik = len(free)
    if tik > 0: # if empty place x somewhere in the list
        this = randrange(tik)
        row, col = free[this]
        board[row][col] = 'X'

board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # make an empty board
board[1][1] = 'X' # 1st x in the middle
free = MakeListOfFreeFields(board)
myturn = True 
while len(free):
    DisplayBoard(board)
    if myturn:
        EnterMove(board)
        victory = VictoryFor(board,'O')
    else:   
        DrawMove(board)
        victory = VictoryFor(board,'X')
    if victory != None:
        break
    myturn = not myturn 
    free = MakeListOfFreeFields(board)

DisplayBoard(board)
if victory == 'Tu':
    print("Haz ganado!")
elif victory == 'me':
    print("Perdiste el desafio!")
else:
    print("Han empatado")