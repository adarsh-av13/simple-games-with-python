def printboard(mat):
  print('  ', end=' ')
  for i in range(len(mat)):
      print(f' {i}', end='  ')
  print()
  for i in range(len(mat)):
    print(f"{i} |", end=" ")
    for j in range(len(mat[i])):
      print(mat[i][j], end=" | ") 
    print("")
  print("")