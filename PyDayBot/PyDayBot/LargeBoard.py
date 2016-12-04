from SmallBoard import *

class LargeBoard(object):
    """description of class"""

    def __init__(self, **kwargs):
        self.tables = [[SmallBoard() for x in range(3)] for x in range(3)]
        self.currentTableIndex = (0, 0)
        self.currentTableLetter = ""
        self.LastMove = ""
        
        return super().__init__(**kwargs)

    def MakeMoveByLetters(self, owner, move):
        boardNumber = ord(move[0]) - ord("A")
        moveNumber = ord(move[1]) - ord("A")

        boardIndexX = int(boardNumber / 3)
        boardIndexY = boardNumber % 3

        self.tables[boardIndexX][boardIndexY].MakeMoveByNumber(owner, moveNumber)
        self.LastMove = move
        self.lastTable = (boardIndexX, boardIndexY)
        self.currentTableIndex = (int(moveNumber / 3), moveNumber % 3)
        self.currentTableLetter = move[1]
    
    def MakeMoveByIndex(self, owner, indexMove):
        move = chr(3 * indexMove[0][1] + indexMove[0][0] + ord("A"))
        move = move + chr(3 * indexMove[1][1] + indexMove[1][0] + ord("A"))

        boardNumber = ord(move[0]) - ord("A")
        moveNumber = ord(move[1]) - ord("A")

        boardIndexX = int(boardNumber / 3)
        boardIndexY = boardNumber % 3

        self.tables[boardIndexX][boardIndexY].MakeMoveByNumber(owner, moveNumber)
        self.LastMove = move
        self.lastTable = (boardIndexX, boardIndexY)
        self.currentTableIndex = (int(moveNumber / 3), moveNumber % 3)
        self.currentTableLetter = move[1]

    def GetCurrentBoard(self):
        return self.tables[self.currentTableIndex[0]][self.currentTableIndex[1]]

    def GetCapturedBoards(self):
        caped = [[0 for x in range(3)] for x in range(3)]
        for x in range(3):
            for y in range(3):
                caped[x][y] = self.tables[x][y].IsCaptured()

        return caped

    def GetLegalMovesByLetter(self):
        list = []
        temp = []
        if self.GetCurrentBoard().IsCaptured() != 0 or self.GetCurrentBoard().IsFull():
            for i in range(3):
                for j in range(3):
                    if self.tables[i][j].IsCaptured() == 0 and not self.tables[i][j].IsFull():
                        temp = self.tables[i][j].GetLegalMovesByLetter()
                        for x in range(len(temp)):
                            temp[x] = chr((3 * i + j) + ord("A")) + temp[x]
                        list += temp
        else:
            temp = self.GetCurrentBoard().GetLegalMovesByLetter()
            for x in range(len(temp)):
                temp[x] = self.currentTableLetter + temp[x]
            list += temp

        return list