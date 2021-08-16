def printsample():
  k = 0
  for i in range(3):
    print("|", end=" ")
    for j in range(3):
      print(k, end=" | ")
      k += 1
    print("")
  print("")

def printboard(mat):
  for i in range(3):
    print("|", end=" ")
    for j in range(3):
      print(mat[i][j], end=" | ") 
    print("")
  print("")
