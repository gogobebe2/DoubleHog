__author__ = 'william'

import time
import sys
import random

from Utils import Enums, Getch, Ascii

# In case run with python 2 instead of 3....
if sys.version_info[0] == 2:
    def input(text):
        # noinspection PyUnresolvedReferences
        return raw_input(text)

menuStates = Enums.enum(START=Ascii.menuStart, RULES=Ascii.menuRules, EXIT=Ascii.menuExit)
turnStates = Enums.enum(ROLE_CHOOSE=Ascii.roleLabel_choose, ROLE=Ascii.roleLabel, PASS_CHOOSE=Ascii.passLabel_choose,
                        PASS=Ascii.passLabel)

def displayScore(players, scores):
    time.sleep(3)
    Ascii.clear()
    print(Ascii.score)

    message = "\n" + (4 - len(players)) * "\t"
    for p in range(0, len(players)):
        message += "\t" + players[p]
        if p != len(players) - 1:
            message += "\t | "
    print(message)

    message = (4 - len(scores)) * "\t"
    for s in range(0, len(scores)):
        message += "\t" + str(scores[s])
        if s != len(scores) - 1:
            message += "\t | "
    print(message)
    time.sleep(7)

def startGame():
    try:
        Ascii.clear()
        print("\n\n\t\t\tAwesome! Lets get started then...")
        while True:
            try:
                amountPlayers = int(input("\n How many players will you be playing with? (2-4 are the limits): "))
                if amountPlayers not in [2, 3, 4]:
                    raise ValueError
            except ValueError:
                for i in range(3):
                    Ascii.clear()
                    print(" Error! You did not enter a valid number! (2-4 are the limits)")
                    time.sleep(1)
                Ascii.clear()
            else:
                break
        players = []
        scores = []
        name = input("\n\n\t Ok cool! We got " + str(amountPlayers) + " players. So what's your name? ")
        players.append(Ascii.capStart(name))
        scores.append(0)

        for player in range(amountPlayers - 1):
            if len(players) == 1:
                name = input("\n\n\t Ok " + players[0] + " and your friend's name? ")
                players.append(Ascii.capStart(name))
                scores.append(0)
            else:
                name = input("\n\n\t Great! And your other friend's name? ")
                players.append(Ascii.capStart(name))
                scores.append(0)

        time.sleep(1)

        message = "\n\n\tGreat! so we have "

        # Shuffled so the order at which they role dice is random.
        random.shuffle(players)
        for index in range(len(players)):
            if index == len(players) - 1:
                if not len(players) == 2:
                    message += "and finally " + players[index]
                else:
                    message += "and " + players[index]
            else:
                if not (len(players) == 2 or index == len(players) - 2):
                    message += players[index] + ", "
                else:
                    message += players[index] + " "
        print(message + "\n\t(Please forgive me if I mis-pronounced your name. I'm only a robot!)")

        time.sleep(3)

        while True:
            cont = True
            index = 0
            for player in players:
                for i in range(0, 1):
                    Ascii.clear()

                    print(Ascii.roleLabel + Ascii.getdiceAnimation1(player) + Ascii.passLabel)

                    time.sleep(1)

                    Ascii.clear()
                    print(Ascii.roleLabel + Ascii.getdiceAnimation2(player) + Ascii.passLabel)
                    time.sleep(1)

                roleState = turnStates.ROLE_CHOOSE
                passState = turnStates.PASS

                Ascii.clear()
                print(roleState + Ascii.getdiceAnimation1(player) + passState)

                getch = Getch._Getch()
                while True:
                    Ascii.clear()
                    print(roleState + Ascii.getdiceAnimation1(player) + passState)
                    key = ord(getch())
                    if key == Getch.DOWN_KEY:
                        if roleState == turnStates.ROLE_CHOOSE:
                            roleState = turnStates.ROLE
                            passState = turnStates.PASS_CHOOSE
                    elif key == Getch.UP_KEY:
                        if passState == turnStates.PASS_CHOOSE:
                            roleState = turnStates.ROLE_CHOOSE
                            passState = turnStates.PASS
                    elif key == Getch.ENTER_KEY:
                        playerScore = scores[players.index(player)]
                        if passState == turnStates.PASS_CHOOSE:
                            Ascii.clear()
                            print("\n\n\n\n\t\t\t\t  You chose to pass...")
                            print(Ascii.arrow)
                            time.sleep(4)
                            displayScore(players, scores)
                            break
                        elif roleState == turnStates.ROLE_CHOOSE:
                            scores[index] = role(playerScore)
                            displayScore(players, scores)
                            break

                for score in scores:
                    if score >= 100:
                        # This means the player has won
                        cont = False
                        break
                index += 1
            if cont:
                continue
            else:
                # TODO:
                # Make player win
                for index in range(0, len(players)):
                    if scores[index] >= 100:
                        print("\n\n\n\n\t\t\t\t  " + players[index] + " wins!")
                        break
                time.sleep(5)
                init()
                break
    except KeyboardInterrupt:
        exitGame()


def exitGame():
    Ascii.clear()
    print("\n\n\n\n\t\t\t\t  Goodbye! :(")
    time.sleep(4)
    exit()


def role(score):
    Ascii.clear()
    dice1 = random.randrange(1, 6)
    dice2 = random.randrange(1, 6)
    for i in range(2):
        print("\n\n\n\n\t\t\t\t  Rolling...")
        print(Ascii.rollingDice1)
        time.sleep(1)
        Ascii.clear()
        print("\n\n\n\n\t\t\t\t  Rolling...")
        print(Ascii.rollingDice2)
        time.sleep(1)
        Ascii.clear()

    diceAni1 = Ascii.diceRoles.get(dice1)
    diceAni2 = Ascii.diceRoles.get(dice2)
    print("\n\n\n\n\n\n\n\n\t\t\t\t" + diceAni1[0:7] + "\t" + diceAni2[0:7])
    print("\t\t\t\t" + diceAni1[7:14] + "\t" + diceAni2[7:14])
    print("\t\t\t\t" + diceAni1[14:] + "\t" + diceAni2[14:])

    youRolledMsg = "\n\n\t\t\tYou rolled "
    if dice1 == dice2:
        youRolledMsg += "2 " + str(dice1) + "'s"
    else:
        youRolledMsg += "a " + str(dice1) + " and a " + str(dice2)

    print(youRolledMsg)

    time.sleep(3)

    if dice1 == 1 or dice2 == 1:
        if dice1 == dice2:
            # Double 1
            score += 25
            print("\t\t" + str(score) + " points will be added to your score...")
        else:
            # Single 1
            score = score - (dice1 + dice2)
            print("\t\t" + str(dice1 + dice2) + " points will be deducted from your score...")

    elif dice1 == dice2:
        # Regular double.
        score += 2 * (dice1 + dice2)
        print("\t\t" + str(2 * (dice1 + dice2)) + " points will added to your score...")
    else:
        # All other cases.
        score += dice1 + dice2
        print("\t\t" + str(dice1 + dice2) + " points will be added to your score...")
    print("\t\tYou now have " + str(score) + " points")
    return score


def displayRules():
    rules = Ascii.rules
    min = 1
    max = 17
    changed = True

    getch = Getch._Getch()
    while True:
        if changed:
            Ascii.clear()
            print(rules[0])
            for lineNumber in range(min, max):
                print(rules[lineNumber])
            print(Ascii.okButtonRules)
            changed = False
        key = ord(getch())
        if key == Getch.ENTER_KEY:
            init()
            break
        elif key == Getch.DOWN_KEY or key == Getch.RIGHT_KEY:
            if max != len(rules):
                min += 1
                max += 1
                changed = True
        elif key == Getch.UP_KEY or key == Getch.LEFT_KEY:
            if min != 1:
                min -= 1
                max -= 1
                changed = True


def init():
    getch = Getch._Getch()
    currentState = menuStates.START
    Ascii.clear()
    print(Ascii.menuStart)

    while True:
        key = ord(getch())
        if key == Getch.ENTER_KEY and currentState == menuStates.START:
            startGame()
            break

        elif key == Getch.ENTER_KEY and currentState == menuStates.EXIT:
            exitGame()
            break

        elif key == Getch.ENTER_KEY and currentState == menuStates.RULES:
            displayRules()
            break
        else:
            states = [menuStates.START, menuStates.RULES, menuStates.EXIT]
            if key == Getch.LEFT_KEY:
                if states.index(currentState) == 0:
                    currentState = states[2]
                else:
                    currentState = states[states.index(currentState) - 1]
            elif key == Getch.RIGHT_KEY:
                if states.index(currentState) == 2:
                    currentState = states[0]

                else:
                    currentState = states[states.index(currentState) + 1]
            Ascii.clear()
            print(currentState)


# If this is run directly, start the program.
if __name__ == '__main__':
    init()