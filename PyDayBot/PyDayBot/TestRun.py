from SmallBoard import *
from PyDayBot import *

board = SmallBoard()

board.table = [[1, 0, -1],[-1, -1, 0],[0, 0, 0]]

data = DamageControl(board)

for i in range(3):
    format = ""
    for j in range(3):
        format += str(board.table[i][j]) + ", "
    print(format)

print()

for i in range(3):
    format = ""
    for j in range(3):
        format += str(data[i][j]) + ", "
    print(format)