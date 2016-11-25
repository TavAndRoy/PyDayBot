from LargeBoard import *
from SmallBoard import *
from PyDayBot import *
from BotAPI import *

MainBoard = LargeBoard()


smallTest = SmallBoard()
smallTest.table = [[1,0,1],[-1,1,0],[0,0,-1]]
temp1 = OffenseControlSmall(smallTest)
temp2 = DamageControlSmall(smallTest)
for i in range(3):
    str1 = ""
    for j in range(3):
        str1 += (str(temp1[i][j] + temp2[i][j]) + ", ")
    print(str1)


def main():
    start_bot(Play, Logger, PORT_NUMBER)

def Logger(data):
    global MainBoard

    MainBoard.tables.clear()
    MainBoard = LargeBoard()
    print("New Connection Recived")
    return "T&R".encode()

def Play(move):

    global MainBoard

    if move == "NN":
        myMove = "EE"
    else:
        MainBoard.MakeMoveByLetters(-1, move)
        myMove = SelectMove(MainBoard)
    
    MainBoard.MakeMoveByLetters(1, myMove)
    print("Sending to server: " + myMove)
    return myMove.encode()























if __name__ == "__main__":
    main()