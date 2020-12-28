"""Tic Tac Toe Game with Python3
    Created by : Amor Ali
    DSI2.1
"""
from random import *

placeDisponibility = [False for i in range(9)]  # what is the valid places with a mono dimension liste
player1Tab = [False for i in range(9)]  # player 1 choices
cpuTab = [False for i in range(9)]  # cpu choices
TicTacToe = [i+1 for i in range(9)]  # table to fill with X or O
player1 = True  # player 1 is Role (the user)
cpu = False  # CPU is waiting player 1 (the computer)
roundNumber = 0  # How many round they play


def gameWinnerTest(liste, a, b, c):
    """Verify the game state is finished or not and who is the winner"""
    return liste[a - 1] == liste[b - 1] == liste[c - 1] == True;


def winnerVerification(liste):
    """Verify game stat"""
    if (gameWinnerTest(liste, 1, 2, 3) == True or gameWinnerTest(liste, 1, 4, 7) == True \
        or gameWinnerTest(liste, 3, 6, 9) == True or gameWinnerTest(liste, 7, 8, 9) == True \
        or gameWinnerTest(liste, 3, 5, 7) == True or gameWinnerTest(liste, 1, 5, 9) == True \
        or gameWinnerTest(liste, 2, 5, 8) == True or gameWinnerTest(liste, 4, 5, 6)) and (roundNumber >= 5):

        return 1  # Someone won the game
    elif roundNumber >= 9:
        return 2  # game null
    return 3  # game don't finish yet


def displayDispoPlaces(liste):
    """Display the empty places"""
    print("Disponible Places now: ", end=" ")
    for i in range(9):
        if not liste[i]:
            print(i + 1, end=" ")
    print("\n")

def inputControl(userInput):
    """Verify the inputted value"""
    if userInput in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return True
    return False


def cpuChoice():
    """Return a random value"""
    randChoice = randint(1, 9)
    return randChoice


def cpuWinCelebration():
    """Return a random comment when the pc win"""
    randCeleb = randint(0, 4)
    celebrateListe = ["Easy peasy lemon squeezy", "Noob don't challenge me again", "I won", "Please uninstall", "I'm unbeatable"]
    return celebrateListe[randCeleb]


placeDisponibility[4] = True
cpuTab[4] = True
TicTacToe[4] = 'X'  # add O for player 2
roundNumber = roundNumber + 1
"""Display game table"""
for i in range(9):
    print("\t|", TicTacToe[i], "|", end=" ")
    if i in [2, 5, 8]:
        print(" ")
print(" ")
while roundNumber <= 9:
    if player1:
        displayDispoPlaces(placeDisponibility)
        userInput = int(input("Player 1 choose a place "))
        if not inputControl(userInput):  # Value not between 1 and 9
            print("You are only allowed to put a number between 1 and 9")
            continue
        if placeDisponibility[userInput-1]:
            print("Already chosen")
            continue
        placeDisponibility[userInput-1] = True
        player1Tab[userInput-1] = True
        player1 = False
        cpu = True
        roundNumber = roundNumber+1
        TicTacToe[userInput - 1] = 'O'  # add X for player 1
        """Display game table"""
        for i in range(9):
            print(TicTacToe[i], "\t", end=" ")
            if i in [2, 5, 9]:
                print("")
        print("")
        if winnerVerification(player1Tab) == 1:
            print("Congrats Player N°1 you won the game")
            break
        elif winnerVerification(player1Tab) == 2:
            print("Nice Try but game null")
            break
    elif cpu:
        cpuInput = cpuChoice()
        if placeDisponibility[cpuInput-1]:
            cpuInput = cpuChoice()
            continue
        displayDispoPlaces(placeDisponibility)
        print("CPU:\"My Turn\": ", cpuInput)
        placeDisponibility[cpuInput - 1] = True
        cpuTab[cpuInput - 1] = True
        player1 = True
        cpu = False
        roundNumber = roundNumber+1
        TicTacToe[cpuInput - 1] = 'X'  # add O for player 2
        """Display game table"""
        for i in range(9):
            print(TicTacToe[i], "\t", end=" ")
            if i in [2, 5, 9]:
                print("")
        print("")
        if winnerVerification(cpuTab) == 1:
            print("CPU:\"", cpuWinCelebration(), "\"")
            break
        elif winnerVerification(cpuTab) == 2:
            print("Nice but game null")
            break

print("***Game finished***")
userQuit = input("Press any key to exit ")  # an input to hold the console from exiting directly
