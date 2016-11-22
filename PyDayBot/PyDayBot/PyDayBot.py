SINGLETONE = 1
DOUBLETONE = 10

def DamageControl(board):
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
        