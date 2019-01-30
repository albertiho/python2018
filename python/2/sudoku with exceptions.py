def printSudoku(vals):
  if type(vals) != str:
    raise TypeError("Illegal Sudoku type {}".format(type(vals)))
  if len(vals) != 81:
    raise ValueError("Illegal Sudoku length {} != 81".format(len(vals)))
  cry = ""
  for q in vals:
    if q not in ["1","2","3","4","5","6","7","8","9"]:
      cry = cry + str(q + ", ")
  if len(cry) > 0:
    raise ValueError("Illegal value(s) {} for a Sudoku digit".format(cry[:-2]))
  printed = 0
  for i in range(19):
    if i%6 == 0:
      print("#####################################")
    elif i%2 ==0:
      print("#---+---+---#---+---+---#---+---+---#")
    else:
      for j in range(37):
        if j % 12 == 0:
          print('#', end ="")
        elif j%4 == 0:
          print('|', end ="")
        elif j %2 == 0:
          print(vals[printed], end ="")
          printed+=1
        else:
          print(" ", end ="")
      print()