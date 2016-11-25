from SmallBoard import *
from copy import deepcopy
from math import *

def DamageControlSmall(board, SINGLETONE = 1, DOUBLETONE = 10):
    damageTable = [[0 for x in range(3)] for x in range(3)]
    
    data = board.Split()
    
    for i in range(len(data)):
        
        allyTilesCount = 0
        enemyTilesCount = 0

        emptyTiles = []

        if i < 3:
            for j in range(len(data[i])):

                if data[i][j] == 1:
                    allyTilesCount += 1

                if data[i][j] == -1:
                    enemyTilesCount += 1

                if data[i][j] == 0:
                    emptyTiles.append(j)

            if allyTilesCount > 0:
                continue

            if enemyTilesCount == 1:
                for j in range(3):
                    if j in emptyTiles:
                        damageTable[i][j] += SINGLETONE
            
            if enemyTilesCount == 2:
                damageTable[i][emptyTiles[0]] += DOUBLETONE

            

        elif i < 6:
            for j in range(len(data[i])):

                if data[i][j] == 1:
                    allyTilesCount += 1

                if data[i][j] == -1:
                    enemyTilesCount += 1

                if data[i][j] == 0:
                    emptyTiles.append(j)

            if allyTilesCount > 0:
                continue

            if enemyTilesCount == 1:
                for j in range(3):
                    if j in emptyTiles:
                        damageTable[j][i - 3] += SINGLETONE
            
            if enemyTilesCount == 2:
                damageTable[emptyTiles[0]][i - 3] += DOUBLETONE

        elif i < 7:
            for j in range(len(data[i])):

                if data[i][j] == 1:
                    allyTilesCount += 1

                if data[i][j] == -1:
                    enemyTilesCount += 1

                if data[i][j] == 0:
                    emptyTiles.append(j)

            if allyTilesCount > 0:
                continue

            if enemyTilesCount == 1:
                for j in range(3):
                    if j in emptyTiles:
                        damageTable[j][j] += SINGLETONE
            
            if enemyTilesCount == 2:
                damageTable[emptyTiles[0]][emptyTiles[0]] += DOUBLETONE

        elif i < 8:
            for j in range(len(data[i])):

                if data[i][j] == 1:
                    allyTilesCount += 1

                if data[i][j] == -1:
                    enemyTilesCount += 1

                if data[i][j] == 0:
                    emptyTiles.append(j)

            if allyTilesCount > 0:
                continue

            if enemyTilesCount == 1:
                for j in range(3):
                    if j in emptyTiles:
                        damageTable[j][2 - j] += SINGLETONE
            
            if enemyTilesCount == 2:
                damageTable[emptyTiles[0]][2 - emptyTiles[0]] += DOUBLETONE

    return damageTable

def OffenseControlSmall(board, SINGLETONE = 2, DOUBLETONE = 13):
    offenseTable = [[0 for x in range(3)] for x in range(3)]
    
    data = board.Split()
    
    for i in range(len(data)):
        
        allyTilesCount = 0
        enemyTilesCount = 0

        emptyTiles = []

        if i < 3:
            for j in range(len(data[i])):

                if data[i][j] == 1:
                    allyTilesCount += 1

                if data[i][j] == -1:
                    enemyTilesCount += 1

                if data[i][j] == 0:
                    emptyTiles.append(j)

            if enemyTilesCount > 0:
                continue

            if allyTilesCount == 1:
                for j in emptyTiles:
                    offenseTable[i][j] += SINGLETONE
            
            if allyTilesCount == 2:
                offenseTable[i][emptyTiles[0]] += DOUBLETONE

            

        elif i < 6:
            for j in range(len(data[i])):

                if data[i][j] == 1:
                    allyTilesCount += 1

                if data[i][j] == -1:
                    enemyTilesCount += 1

                if data[i][j] == 0:
                    emptyTiles.append(j)

            if enemyTilesCount > 0:
                continue

            if allyTilesCount == 1:
                for j in emptyTiles:
                    offenseTable[j][i - 3] += SINGLETONE
            
            if allyTilesCount == 2:
                offenseTable[emptyTiles[0]][i - 3] += DOUBLETONE

        elif i < 7:
            for j in range(len(data[i])):

                if data[i][j] == 1:
                    allyTilesCount += 1

                if data[i][j] == -1:
                    enemyTilesCount += 1

                if data[i][j] == 0:
                    emptyTiles.append(j)

            if enemyTilesCount > 0:
                continue

            if allyTilesCount == 1:
                for j in emptyTiles:
                    offenseTable[j][j] += SINGLETONE
            
            if allyTilesCount == 2:
                offenseTable[emptyTiles[0]][emptyTiles[0]] += DOUBLETONE

        elif i < 8:
            for j in range(len(data[i])):

                if data[i][j] == 1:
                    allyTilesCount += 1

                if data[i][j] == -1:
                    enemyTilesCount += 1

                if data[i][j] == 0:
                    emptyTiles.append(j)

            if enemyTilesCount > 0:
                continue

            if allyTilesCount == 1:
                for j in range(3):
                    if j in emptyTiles:
                        offenseTable[j][2 - j] += SINGLETONE
            
            if allyTilesCount == 2:
                offenseTable[emptyTiles[0]][2 - emptyTiles[0]] += DOUBLETONE

    return offenseTable

def DamageControlLarge(board):
    tempBoard = SmallBoard.FromList(board.GetCapturedBoards())
    return DamageControlSmall(tempBoard, 100, 1000)

def OffenseControlLarge(board):
    tempBoard = SmallBoard.FromList(board.GetCapturedBoards())
    return OffenseControlSmall(tempBoard, 130, 9999999)

def SelectMove(board):
    print("Current Table:" + board.currentTableLetter)
    print("Current Table Values:" + str(board.GetCurrentBoard().table))
    moves = board.GetLegalMovesByLetter()

    print("Tested Moves: " + str(moves))

    maxDamage = MeasureMove(board, moves[0])
    bestMove = moves[0]
    for move in moves:
        damage = MeasureMove(board, move)
        print("Move: " + str(move) + " Damage: " + str(damage))
        if (maxDamage < damage):
            maxDamage = damage
            bestMove = move

    return bestMove

def MeasureMove(board, move):
    largeWorkBoard = deepcopy(board)
    mySmallWorkBoard = largeWorkBoard.GetCurrentBoard()
    
    largeBaseDamage = DamageControlLarge(largeWorkBoard)
    mySmallBaseDamage = DamageControlSmall(mySmallWorkBoard)
    largeBaseOffense = OffenseControlLarge(largeWorkBoard)
    mySmallBaseOffense = OffenseControlSmall(mySmallWorkBoard)
    
    largeWorkBoard.MakeMoveByLetters(1, move)

    largePostDamage = DamageControlLarge(largeWorkBoard)
    largePostOffense = OffenseControlLarge(largeWorkBoard)
    mySmallPostDamage = DamageControlSmall(mySmallWorkBoard)
    nextSmallPostDamage = DamageControlSmall(largeWorkBoard.GetCurrentBoard())

    sum = 0
    for i in range(3):
        for j in range(3):
            sum += sqrt((mySmallBaseOffense[i][j] + largePostOffense[i][j]) * (largePostDamage[i][j] + mySmallPostDamage[i][j] + nextSmallPostDamage[i][j]))
            

    return sum