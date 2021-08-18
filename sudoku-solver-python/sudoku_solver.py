def find_next_empty(sudoku,r,c):
    while r<9:
        c1 = 0
        while c1<9:
            if sudoku[r][c1] == 0:
                return r,c1
            c1 += 1
        r += 1
    
    return -1,-1

def try_move(sudoku,x,r,c):

    sr = 3*(r//3)
    sc = 3*(c//3)
    #check in box
    for i in range(sr,sr+3):
        for j in range(sc,sc+3):
            if(i==r and j==c):
                continue
            if(sudoku[i][j] == x):
                return False
    
    #check in row
    for i in range(9):
        if(i==c):
            continue
        if(sudoku[r][i] == x):
            return False
    
    #check in column
    for i in range(9):
        if(i==r):
            continue
        if(sudoku[i][c] == x):
            return False
    return True

def try_next_move(sudoku,r,c):
    r, c =  find_next_empty(sudoku,r,c)
    if r==-1 and c==-1:
        return True
    for i in range(1,10):
        sudoku[r][c] = i        
        res = try_move(sudoku,i,r,c)
        if res == True:
            res2 = try_next_move(sudoku,r,c)
            if res2 == True:
                return True
            else:
                sudoku[r][c] = 0
        else:
            sudoku[r][c] = 0
    return False        



def solve(sudoku):
    result = try_next_move(sudoku,0,0)
    return result

print("Enter Sudoku: ")
sudoku = []
for i in range(9):
    x = input()
    y = x.split(' ')
    sudoku.append(y)
for i in range(9):
    for j in range(9):
        sudoku[i][j] = int(sudoku[i][j])
result = solve(sudoku)
if result == True:
    print("\nSolution:")
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end=" ")
        print("")
else:
    print("Incorrect Puzzle")