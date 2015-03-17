__author__ = 'william'

import Ascii
import Getch
import platform
import Enums

if platform.system() == "Windows":
    ENTER_KEY = 13
    LEFT_KEY = 75
    RIGHT_KEY = 77
elif platform.system() == "Linux":
    ENTER_KEY = 13
    LEFT_KEY = 68
    RIGHT_KEY = 67

menuStates = Enums.enum(START=Ascii.menuStart, RULES=Ascii.menuRules, EXIT=Ascii.menuExit)


def startGame():
    pass

def displayRules():
    Ascii.clear()
    print(Ascii.rules)
    print(Ascii.okButton)
    getch = Getch._Getch()
    while True:
        key = ord(getch())
        if key == ENTER_KEY:
            init()
            break


def init():
    getch = Getch._Getch()
    currentState = menuStates.START
    Ascii.clear()
    print(Ascii.menuStart)

    while True:
        key = ord(getch())
        if key == ENTER_KEY and currentState == menuStates.START:
            startGame()
            break

        elif key == ENTER_KEY and currentState == menuStates.EXIT:
            exit()
            break

        elif key == ENTER_KEY and currentState == menuStates.RULES:
            displayRules()
            break
        else:
            states = [menuStates.START, menuStates.RULES, menuStates.EXIT]
            if key == LEFT_KEY:
                if states.index(currentState) == 0:
                    currentState =  states[2]
                else:
                    currentState =  states[states.index(currentState) - 1]
            elif key == RIGHT_KEY:
                if states.index(currentState) == 2:
                    currentState =  states[0]

                else:
                    currentState =  states[states.index(currentState) + 1]
            Ascii.clear()
            print(currentState)


#if the file is the main file then start the program
if __name__ == '__main__':
    init()