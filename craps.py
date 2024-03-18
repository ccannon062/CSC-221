# craps.py
# Caleb Cannon
# A program that simulates multiple games of craps

import random

def getinput():
    print("1. Two dices are required to play and a player rolls two six-sided dice and adds the numbers rolled together")
    print("2. If on the first roll a player encounters a total of 7 or 11 the player automatically wins, and if the player rolls a total of 2, 3, or 12 the player automatically loses, and play is over")
    print("3. If a player rolls a total of 4, 5, 6, 8, 9, or 10 on their first roll, that number becomes the ‘point. Then the player continues to roll the two dice again until one of two things happens either they roll the ‘point’ again, in which case they win, or they roll a 7, in which case they lose.")
    n = int(input("How many games would you like to play? "))
    input("Press enter to continue ")
    return n
    
def rolldice():
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    total = die1 + die2
    return total

def play1game():
    value = rolldice()
    if value == 2 or value == 12 or value == 3:
        return "Loss"
    elif value == 7 or value == 11:
        return "Win"
    else:
        result = roll4point(value)
        return result
        
def roll4point(value):
     roll = value
     while roll:
         roll = rolldice()
         if roll == 7:
            return "Loss"
         elif roll == 11:
            return "Win"
         else:
            roll = rolldice()
            
def playngames(n):
    wins = 0
    losses = 0
    result = play1game()
    if result == "Win":
        wins = wins + 1
    else:
        losses = losses + 1
    for items in range(n-1):
        result = play1game()
        if result == "Win":
            wins = wins + 1
        else:
            losses = losses + 1
    return wins, losses

def main():
    n = getinput()
    wins, losses = playngames(n)
    winprob = wins/n
    lossprob = losses/n
    print("Wins:",wins)
    print("Win probability:",round(winprob,3))
    print("Losses:",losses)
    print("Loss probability:",round(lossprob,3))
main()
    
