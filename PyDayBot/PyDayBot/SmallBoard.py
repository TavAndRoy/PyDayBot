from math import *
from copy import deepcopy

class SmallBoard(object):
    """Helps calculating the samll boards"""

    def __init__(self, **kwargs):
        self.table = [[0 for x in range(3)] for x in range(3)]
        
        return super().__init__(**kwargs)

    def GetLegalMovesByIndex(self):
        return [ (x,y) for x in range(3) for y in range(3) if self.table[x][y] == 0]

    def GetLegalMovesByLetter(self):
        return [ chr((3 * x + y) + ord("A")) for x in range(3) for y in range(3) if self.table[x][y] == 0]

    def MakeMoveByLetter(self, owner, move):
        value = ord(move) - ord("A")
        x = int(value / 3.0)
        y = value % 3
        self.table[x][y] = owner

    def MakeMoveByNumber(self, owner, move):
        x = int(move / 3)
        y = move % 3
        self.table[x][y] = owner

    def MakeMoveByIndex(self, owner, index):
        self.table[index[0]][index[1]] = owner

    def Split(self):
        links = [[0 for x in range(3)] for x in range(8)]
        
        for i in range(3):
            for j in range(3):
                links[i][j] = self.table[i][j]

        for i in range(3):
            for j in range(3):
                links[i + 3][j] = self.table[j][i]

        for i in range(3):
            links[6][i] = self.table[i][i]

        for i in range(3):
            links[7][i] = self.table[i][2 - i]

        return links

    def IsCaptured(self):
        data = self.Split()
        
        for item in data:
            flag = True
            
            for index in range(2):
                if (item[index] != item[index + 1] or item[index] == 0):
                    flag = False
                    break

            if (flag):
                return item[0]

        return 0

    def IsFull(self):
        for i in range(3):
            for j in range(3):
                if self.table[i][j] == 0:
                    return False
        return True

    @staticmethod
    def FromList(data):
        board = SmallBoard()
        board.table = deepcopy(data)

        return board