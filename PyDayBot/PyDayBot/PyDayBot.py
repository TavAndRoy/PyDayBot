from SmallBoard import *
from copy import deepcopy
from math import *
import multiprocessing as mp

def DamageControlSmall(board, SINGLETONE=1, DOUBLETONE=10):
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

def OffenseControlSmall(board, SINGLETONE=2, DOUBLETONE=13):
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
                for j in emptyTiles:
                        offenseTable[j][2 - j] += SINGLETONE
            
            if allyTilesCount == 2:
                offenseTable[emptyTiles[0]][2 - emptyTiles[0]] += DOUBLETONE

    return offenseTable

def DamageControlLarge(board, SINGLETONE=100, DOUBLETONE=1000):
    tempBoard = SmallBoard.FromList(board.GetCapturedBoards())
    return DamageControlSmall(tempBoard, SINGLETONE, DOUBLETONE)

def OffenseControlLarge(board, SINGLETONE=130, DOUBLETONE=9000):
    tempBoard = SmallBoard.FromList(board.GetCapturedBoards())
    return OffenseControlSmall(tempBoard, SINGLETONE, DOUBLETONE)

def SVMeasureMove(data):
    return MeasureMove(data[0], data[1])

def MeasureMove(board, move):
    coordinates = parseMove(move)
    largeWorkBoard = deepcopy(board)
    currSmallWorkBoard = deepcopy(largeWorkBoard.tables[coordinates[0][0]][coordinates[0][1]])

    targetBoardDamage = DamageControlSmall(currSmallWorkBoard)
    moveDamageValue = targetBoardDamage[coordinates[1][0]][coordinates[1][1]]

    targetBoardOffense = OffenseControlSmall(currSmallWorkBoard)
    moveOffenseValue = targetBoardOffense[coordinates[1][0]][coordinates[1][1]]

    largeBoardDamage = DamageControlLarge(largeWorkBoard)
    largeBoardOffense = OffenseControlLarge(largeWorkBoard)

    largeWorkBoard.MakeMoveByLetters(1, move)

    largeBoardDamageValue = 0
    largeBoardOffenseValue = 0

    moveCaptureBoard = False
    if largeWorkBoard.tables[coordinates[0][0]][coordinates[0][1]].IsCaptured() == 1:
        moveCaptureBoard = True

    if moveCaptureBoard:
        largeBoardDamageValue = largeBoardDamage[coordinates[0][0]][coordinates[0][1]]
        largeBoardOffenseValue = largeBoardOffense[coordinates[0][0]][coordinates[0][1]]

    enemyMoveOffenseValue = 0
    enemyMoveDamageValue = 0
    enemyLargeBoardDamageValue = 0
    enemyLargeBoardOffenseValue = 0

    maxSum = 0

    if largeWorkBoard.tables[coordinates[1][0]][coordinates[1][1]].IsCaptured() == 0:
        enemyTargetBoardOffense = DamageControlSmall(largeWorkBoard.tables[coordinates[1][0]][coordinates[1][1]], 2, 13)
        enemyMoveOffenseValue = max(max(enemyTargetBoardOffense))

        enemyTargetBoardDamage = OffenseControlSmall(largeWorkBoard.tables[coordinates[1][0]][coordinates[1][1]], 1, 10)
        enemyMoveDamageValue = max(max(enemyTargetBoardDamage))

        enemyMaxValue = -1
        enemyMoveCoords = (0,0)

        for i in range(3):
            for j in range(3):
                if enemyMaxValue < enemyTargetBoardDamage[i][j] + enemyTargetBoardOffense[i][j]:
                    enemyMaxValue = enemyTargetBoardDamage[i][j] + enemyTargetBoardOffense[i][j]
                    enemyMoveCoords = (i,j)

        enemyLargeBoardDamage = OffenseControlLarge(largeWorkBoard, 90, 900)
        enemyLargeBoardOffense = DamageControlLarge(largeWorkBoard, 100, 7500)
    
        largeWorkBoard.MakeMoveByIndex(-1, (coordinates[1],enemyMoveCoords))

        if largeWorkBoard.tables[coordinates[1][0]][coordinates[1][1]].IsCaptured() == -1:
            enemyLargeBoardDamageValue = enemyLargeBoardDamage[coordinates[1][0]][coordinates[1][1]]
            enemyLargeBoardOffenseValue = enemyLargeBoardOffense[coordinates[1][0]][coordinates[1][1]]

        maxSum = enemyMoveDamageValue + enemyMoveOffenseValue + enemyLargeBoardDamageValue + enemyLargeBoardOffenseValue
    else:
        availableMoves = largeWorkBoard.GetLegalMovesByLetter()
        for possibleMove in availableMoves:
            secondLargeWorkBoard = deepcopy(largeWorkBoard)
            tempCoords = parseMove(possibleMove)
            
            enemyTargetBoardOffense = DamageControlSmall(secondLargeWorkBoard.tables[tempCoords[0][0]][tempCoords[0][1]], 2, 8)
            enemyMoveOffenseValuePrivate = max(max(enemyTargetBoardOffense))

            enemyTargetBoardDamage = OffenseControlSmall(secondLargeWorkBoard.tables[tempCoords[0][0]][tempCoords[0][1]], 1, 6)
            enemyMoveDamageValuePrivate = max(max(enemyTargetBoardDamage))

            enemyMaxValue = -1
            enemyMoveCoords = (0,0)

            for i in range(3):
                for j in range(3):
                    if enemyMaxValue < enemyTargetBoardDamage[i][j] + enemyTargetBoardOffense[i][j]:
                        enemyMaxValue = enemyTargetBoardDamage[i][j] + enemyTargetBoardOffense[i][j]
                        enemyMoveCoords = (i,j)

            enemyLargeBoardDamage = OffenseControlLarge(secondLargeWorkBoard, 90, 900)
            enemyLargeBoardOffense = DamageControlLarge(secondLargeWorkBoard, 100, 7500)
    
            secondLargeWorkBoard.MakeMoveByIndex(-1, (tempCoords[0],enemyMoveCoords))

            enemyLargeBoardDamageValuePrivate = 0
            enemyLargeBoardOffenseValuePrivate = 0

            if secondLargeWorkBoard.tables[tempCoords[0][0]][tempCoords[0][1]].IsCaptured() == -1:
                enemyLargeBoardDamageValuePrivate = enemyLargeBoardDamage[tempCoords[0][0]][tempCoords[0][1]]
                enemyLargeBoardOffenseValuePrivate = enemyLargeBoardOffense[tempCoords[0][0]][tempCoords[0][1]]

            maxSum = max(enemyLargeBoardDamageValuePrivate + enemyLargeBoardOffenseValuePrivate + enemyMoveDamageValuePrivate + enemyMoveOffenseValuePrivate, maxSum)
            del secondLargeWorkBoard

    mix = (moveDamageValue + moveOffenseValue + largeBoardDamageValue + largeBoardOffenseValue) - (maxSum)
    print("[Move: " + move + "] [Mix: " + str(mix) + "] [MaxSum: " + str(maxSum) + "]")

    return mix

def parseMove(move):
    boardNumber = ord(move[0]) - ord("A")
    moveNumber = ord(move[1]) - ord("A")

    boardIndexX = int(boardNumber / 3)
    boardIndexY = boardNumber % 3

    smallBoardX = int(moveNumber / 3)
    smallBoardY = moveNumber % 3

    return [(boardIndexX, boardIndexY),(smallBoardX, smallBoardY)]

def SelectMove(board, threadPool):
    moves = board.GetLegalMovesByLetter()

    '''maxDamage = -65535
    bestMove = ""
    for move in moves:
        damage = MeasureMove(board, move)
        if (maxDamage < damage):
            maxDamage = damage
            bestMove = move

    return bestMove'''

    inputs = [(board, move) for move in moves]
    results = threadPool.map(SVMeasureMove, inputs)
    return moves[results.index(max(results))]