import random
import pyfiglet
from printboard import printboard, printsample

header=pyfiglet.figlet_format("tic - tac - toe")
print(f"{header}")
printsample()
flag = 0
gameWon = False
matrix = [[' ' for i in range(3)] for j in range(3)]

filled = []
unfilled = [ i for i in range(9) ]
def userTurn():
    c = input(f"Users's turn(X): ")
    if c.isnumeric() == False or (int(c)<0 or int(c)>8):
        print("Invalid input. Enter a number between 0 and 8 only")
    elif int(c) not in unfilled:
        print("The Box you chose is already filled. Choose another")
    else:
        c = int(c)
        unfilled.remove(c)
        matrix[c//3][c%3] = 'X'

def isGameWon():
    #checkRows
    for i in range(3):
        if(matrix[i][0] == matrix[i][1] and matrix[i][1] == matrix[i][2] and matrix[i][0] != ' '):
            return matrix[i][0], True
    #checkColumns
    for i in range(3):
        if(matrix[0][i] == matrix[1][i] and matrix[1][i] == matrix[2][i] and matrix[0][i] != ' '):
            return matrix[0][i], True
    #checkDiagonals
    if matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2] and matrix[0][0] != ' ':
        return matrix[0][0], True
    if matrix[2][0] == matrix[1][1] and matrix[1][1] == matrix[0][2] and matrix[2][0] != ' ':
        return matrix[2][0], True
    return ' ', False

def computerTurn():
    c = random.choice(unfilled)
    for i in unfilled:
        matrix[i//3][i%3] = 'X'
        _, gameEnd = isGameWon()
        matrix[i//3][i%3] = ' '
        if gameEnd == True:
            c = i
            break
    for i in unfilled:
        matrix[i//3][i%3] = 'O'
        _, gameEnd = isGameWon()
        matrix[i//3][i%3] = ' '
        if gameEnd == True:
            c = i
            break
    print(f"Computer's turn(O): {c}")
    unfilled.remove(c)
    matrix[c//3][c%3] = 'O'

winner = ' '
while unfilled and gameWon == False:
    if flag == 0:
        userTurn()
    else:
        computerTurn()
    winner, gameWon = isGameWon()
    flag = not flag
    printboard(matrix)
if winner == ' ':
    print("It's a tie")
else:
    print(f"{winner} wins")