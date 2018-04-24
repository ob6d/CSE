"""
import random
money = 15
print("You have 15 dollars")
wins = 0
losses = 0
round = 0
most = money
while money > 0:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(dice1)
    print(dice2)
    total = dice1 + dice2
    print(total)
    if total == 7:
        money += 4
        wins += 1
        if most < money:
            most = money
            print(most)
    else:
        money -= 1
        print(money)
        losses += 1
        round += 1

    print("wins %s" % wins)
    print("lose %s" % losses)
    print("round %s" % round)
    print(most)
"""

import random
money = 15
print("You have 15 dollars")
