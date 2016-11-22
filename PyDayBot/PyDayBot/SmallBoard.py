class SmallBoard(object):
    """Helps calculating the samll boards"""

    def __init__(self, **kwargs):
        self.table = [[0 for x in range(3)] for x in range(3)]
        
        return super().__init__(**kwargs)

    def GetLegalMoves():
        return [ (x,y) for x in range(3) for y in range(3) if self.table[x][y] == 0]
