'''
    Folasade Orepo-Orjay and Kairah Foster
    CS111, 01/22/20, hw05
    This is a module which imitates the game of hog.
    This is a two player game in which players choose to roll
    up to ten die, and the first player to reach a score of
    100 or more wins.
'''

import random
import math

'''
    Prompts user to pick any amount of dice between 1 and 10.
    Simulates rolling dice, and generates the total.
    Returns value, unless any ones were rolled, then returns a score of 1.
    dieNum - simulates rolling a dice, generating a random num 1-6.
'''

def rollDice(numDice):
    wantedNum = (1,2,3,4,5,6,7,8,9,10)
    currentScore = 0
    if numDice not in wantedNum:
        print ('Warning! Number has to be between 1-10')
        return currentScore
    for i in range (numDice):
        dieNum = random.randint(1,6)
        currentScore = currentScore + dieNum

    return currentScore

'''
    Returns total number of points once numDice are rolled. If the sum of both scores end in 7, automatically rolls one die in the following turn.
    Score-
    opponentScore-
'''

def takeTurn(score, opponentScore, numDice):
    rollingDice = rollDice(numDice)
    bothScore = opponentScore + score
    if bothScore % 10 == 7:
        numDice = 1
        rollingDice = rollDice(numDice)
    return rollingDice

'''
    A strategy funcion, that returns the number of dice that a player chooses to roll. It will always return 3 dice. However, if the opponent is 6 points away from the goal score and the player's score is less than 70% of the goal score, then 7 die will be rolled. if the player's score is more than 90% of goal score, 2 die will be rolled.
    score-
    opponentScore-
    goalScore-
'''
def roll3UnlessCloseToEnd(score, opponentScore, goalScore):
    goalSix = goalScore - 6
    lessSeven = goalScore < 70
    rollingDice = rollDice(3)
    if opponentScore == goalSix and score == lessSeven:
       rollingDice = rollDice(7)
    if score > 90:
       rollingDice = rollDice(2)
    return(rollingDice)

'''
    This is a strategy function for a human input
    score-
    opponentScore-
    goalScore-
'''
def humanPlayer(score, opponentScore, goalScore):
    print ("Your score", score, "and your opponent's score is", opponentScore)
    numberAsAString = input(' Enter in a number of dice to roll: ')
    newInput = int(numberAsAString)
    print ('you rolled', newInput)
    return newInput


'''
    Simulates a game of hog between 2 players, returns 1 if player 1 wins, 0 if a tie,
    and -1 if player 2 wins.
    goalScore- number of points a player needs to win, 100
    maxRounds- maximum number of times a player gets to play...
    strategy1- A strategy function defined above and passed in as a parameter
    strategy2- A strategy function defined above and passed in as a parameter
'''
    
def playHog(goalScore, maxRounds, strategy1, strategy2):
    score = 0
    opponentScore = 0
    for i in range(maxRounds):

        if i % 2 == 0:
            numDice = humanPlayer(score, opponentScore, 100)
            points = takeTurn(score, opponentScore, numDice)
            score = score + points
        if i % 2 == 1:
            points = roll3UnlessCloseToEnd(score, opponentScore, 100)
            opponentScore = opponentScore + points
        
    if abs(score - goalScore) < abs(opponentScore - goalScore):
        return 1
    if abs(opponentScore - goalScore) < abs(score - goalScore):
        return -1
    if score == opponentScore:
        return 0


def main():
    game = playHog(100, 5, roll3UnlessCloseToEnd, humanPlayer)
    if game == 1 :
        print('Player 1 wins')
    if game == -1 :
        print('Player 2 wins')
    if game == 0:
        print ('Tie!')


    
# These lines will allow you to run your code from the command line
# But if you just import your code into the python interpreter, 
# it won't run automatically
if __name__ == '__main__':
    main()





