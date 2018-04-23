"""You start with $15. Each time you play (round), you make a bet of $1. Two dice (D6) are rolled.
If the sum of the numbers is the number 7, then you win your bet back, plus an additional $4.
When the game is run, it will keep running until you have run out of money.
The program will then display how many rounds it took to run out of money.
Extension: If you finish early, what was the maximum amount of money you had throughout the game?
What round did you have the most money?
"""
import random
money = 15
print("You have 15 dollars")
a = random.randint(1,6)
b = random.randint(1,6)
print(a)
print(b)
print(a + b)
total = (a + b)
round = 0

while money > 0:
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    total = (int(input(a + b)))
    round += 1

    if total == 7:
        money += 4
        print("You have %d dollars" % money)
        print("Round %d" % round)
        break

    if total != 7:
        money -= 1
        print("You have %d dollars" % money)
        print("Round %d" % round)
        break

    elif money == 0:
        print("You lost")
        print("You lasted %d rounds" % round)
