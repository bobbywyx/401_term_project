import random
import numpy
import math
import matplotlib.pyplot as plt

from game_class import GambleGame

# Initial Bankroll
bankroll = 100
bankroll_list = [bankroll]

# Probability
p = 0.6
q = 1 - p

# Increase factor
b = 1

#  Number of rounds to play
num_rounds = 0
num_list = [num_rounds]

info = {
    "id": 0,
    "p": 0.6,
    "q": 0.4,
    "b": 1,
}


def gamble_function(money_in_bet, info):
    if random.random() < info["p"]:
        return (1 + info["b"]) * money_in_bet
    else:
        return 0


def decision_function(history_data, info):
    return info["p"] + (info["p"] - 1) / info["b"]


def ending_condition_function(history_data, info):
    return len(history_data) > 100 or (len(history_data)!=0 and history_data[-1][3] <= 0)


game = GambleGame(bankroll, decision_function, gamble_function, ending_condition_function, info)

game.play()


# while num_rounds <= 100 and bankroll > 0:
#     # Kelly's criterion
#     proportion = p + (p - 1) / b
#     # Bet size
#     Y0 = proportion * bankroll
#
#     if random.random() < p:  # Win
#         Y1 = (1 + b) * Y0
#     else:  # Lose
#         Y1 = 0
#
#     bankroll = bankroll - Y0 + Y1
#     num_rounds += 1
#     num_list.append(num_rounds)
#     bankroll_list.append(bankroll)
#
# plt.title("Simulation of Kelly Criterion")

# get the data from the game object, get the first element of the tuple
bankroll_list = [x[0] for x in game.history_data]
num_list = [x for x in range(len(bankroll_list))]


plt.subplot(1, 2, 1)
plt.plot(num_list, bankroll_list)
plt.xlabel("n")
plt.ylabel("Bankroll")

plt.subplot(1, 2, 2)
plt.plot(num_list, numpy.log10(bankroll_list))
plt.xlabel("n")
plt.ylabel("Bankroll (log scale)")
plt.savefig("figure.png")
