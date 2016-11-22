from SmallBoard import *

class LargeBoard(object):
    """description of class"""

    def __init__(self, **kwargs):
        self.tables = [[SmallBoard() for x in range(3)] for x in range(3)]
        self.currentTable = (0, 0)
        
        return super().__init__(**kwargs)

    def MakeMoveByLetters(owner, move="EE"):
        boardNumber = ord(move[0]) - ord("A")
        moveNumber = ord(move[1]) - ord("A")

        boardIndexX = boardNumber / 3.0
        boardIndexY = boardNumber % 3

        self.tables[boardIndexX][boardIndexY].table[moveIndexX].MakeMoveByNumber(moveNumber)
        self.currentTable = (boardIndexX, boardIndexY)

    def GetCurrentBoard():
        return self.tables[currentTable[0]][currentTable[1]]

