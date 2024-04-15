import random
import numpy
import math
import matplotlib.pyplot as plt

from game_class import GambleGame

# Parameters

# Initial Bankroll
bankroll = 100

# Probability
p = 0.6
q = 1 - p

# Increase factor
b = 1

#  Number of rounds to play
num_rounds = 100

info = {
    "id": 0,
    "p": p,
    "q": q,
    "b": b,
}


# Gamble
def gamble_function(money_in_bet, info):
    if random.random() < info["p"]:
        return (1 + info["b"]) * money_in_bet
    else:
        return 0


def decision_function(history_data, info):
    # return 0.5
    return info["p"] + (info["p"] - 1) / info["b"]


def ending_condition_function(history_data, info):
    return len(history_data) >= num_rounds or (len(history_data) != 0 and history_data[-1][3] <= 0)


game = GambleGame(bankroll, decision_function, gamble_function, ending_condition_function, info)

bankroll_history_of_different_games = []

for i in range(50):
    game.replay()

    bankroll_list = [x[0] for x in game.history_data] + [game.history_data[-1][3]]
    num_list = [x for x in range(len(bankroll_list))]

    if len(bankroll_list) < num_rounds:
        bankroll_list += [bankroll_list[-1]] * (num_rounds - len(bankroll_list) + 1)

    # print(bankroll_list)
    # print(len(bankroll_list))

    bankroll_history_of_different_games.append(bankroll_list)

# plot

x = [x for x in range(len(bankroll_history_of_different_games[-1]))]

fig, ax = plt.subplots()

for i in range(len(bankroll_history_of_different_games)):
    ax.plot(x, numpy.log10(bankroll_history_of_different_games[i]), label='Data ' + str(i))
    # ax.plot(x, (bankroll_history_of_different_games[i]), label='Data ' + str(i))

# get the average of the bankroll history

average_bankroll = numpy.mean(bankroll_history_of_different_games, axis=0)
# print(average_bankroll)

ax.plot(x, numpy.log10(average_bankroll), label='Average', color='red', linewidth=2)

plt.savefig("figure2.png")
