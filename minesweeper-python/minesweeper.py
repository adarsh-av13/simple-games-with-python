import random
import pyfiglet
from printboard import printboard
matrix = [['.' for i in range(8)] for j in range(8) ]
inPlayMatrix = [['.' for i in range(8)] for j in range(8) ]
bombs = []
filledCount = 0

def fillBombs(mat):
    for i in bombs:
        mat[i//8][i%8] = '×'

def countNearbyBombs(r,c):
    count = 0
    for i in range(3):
        if r-1+i<0 or r-1+i>7: continue
        for j in range(3):
            if c-1+j<0 or c-1+j>7: continue
            if i==1 and j==1:
                continue
            if matrix[r-1+i][c-1+j] == '×':
                count += 1
    return count
def fillNumbers():
    for i in range(8):
        for j in range(8):
            if matrix[i][j] == '×':
                continue
            c = countNearbyBombs(i,j)
            matrix[i][j] = c
for i in range(10):
    matrix[i//8][i%8] = '×'
for i in range(10):
    x = random.randint(0,63)
    matrix[i//8][i%8], matrix[x//8][x%8] = matrix[x//8][x%8], matrix[i//8][i%8]
    bombs.append(x)
    
fillBombs(matrix)
fillNumbers()
def playFill(r,c,s):
    global filledCount
    if r>7 or c>7 or r<0 or c<0:
        return False
    if inPlayMatrix[r][c] != '.':
        return False
    inPlayMatrix[r][c] = matrix[r][c]
    filledCount += 1
    if s==0 and matrix[r][c] == '×':
        fillBombs(inPlayMatrix)
        return True
    count = countNearbyBombs(r,c)
    if(count == 0):
        playFill(r-1,c-1,1)
        playFill(r-1,c,1)
        playFill(r-1,c+1,1)
        playFill(r,c-1,1)
        playFill(r,c+1,1)
        playFill(r+1,c-1,1)
        playFill(r+1,c,1)
        playFill(r+1,c+1,1)
    return False
    
gameOver = False
count = 0
header = pyfiglet.figlet_format("minesweeper")
print(f"{header}")
printboard(inPlayMatrix)
while count < 10 and filledCount < 54 and gameOver == False:
    choice = input("Enter Choice: 1 to flag a bomb, 0 to open a square(default): ")
    if choice == '1':
        r = int(input("enter row: "))
        c = int(input("enter column: "))
        inPlayMatrix[r][c] = 'ƒ'
        if matrix[r][c] == '×':
            count += 1
    else:
        r = int(input("enter row: "))
        c = int(input("enter column: "))
        gameOver = playFill(r,c,0)
    printboard(inPlayMatrix)
if count == 10 or filledCount == 54:
    print("You Win")
else:
    print("You Lose")