from LargeBoard import *
from SmallBoard import *
from PyDayBot import *
from BotAPI import *
import multiprocessing
import time

MainBoard = LargeBoard()
turnCount = 0
ThreadPool = None

def main():
    global ThreadPool
    PORT_NUMBER = int(input("Please enter the desired port:"))
    ThreadPool = multiprocessing.Pool(processes = multiprocessing.cpu_count())
    start_bot(Play, Logger, PORT_NUMBER)

def Logger(data):
    global MainBoard, turnCount

    MainBoard = LargeBoard()
    turnCount = 0
    print("New Connection Recived")
    return "T&R".encode()

def Play(move):
    global MainBoard, turnCount

    elpased = 0

    if move == "NN":
        MainBoard = LargeBoard()
        turnCount = 0
        myMove = "EE"
    else:
        MainBoard.MakeMoveByLetters(-1, move)
        turnCount += 1
        start = time.clock()
        myMove = SelectMove(MainBoard, ThreadPool)
        elpased = time.clock() - start
    
    MainBoard.MakeMoveByLetters(1, myMove)
    turnCount += 1
    print("Sending to server: " + myMove)
    print("Turn: " + str(turnCount))
    print("Time: " + str(int(elpased * 1000)) + "ms")
    return myMove.encode()























if __name__ == "__main__":
    main()