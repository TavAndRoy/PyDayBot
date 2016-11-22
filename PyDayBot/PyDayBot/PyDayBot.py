def DamageControl(board):
    damageTable = [[0 for x in range(3)] for x in range(3)]
    
    data = board.Split()
    
    for i in range(len(data)):
        