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

num_experiment = 5000

info = {
    "id": 0,
    "p": p,
    "q": q,
    "b": b,
}

print("game info:", info)
print("num_rounds:", num_rounds)
print("num_experiment:", num_experiment)


# Gamble
def gamble_function(money_in_bet, info):
    if random.random() < info["p"]:
        return (1 + info["b"]) * money_in_bet
    else:
        return 0


def decision_function(history_data, info):
    # return 0.3
    return info["p"] + (info["p"] - 1) / info["b"]
    # return (info["p"]*info["b"] + info["p"] -1) / (info["p"] * info["b"] * info["b"] + 1 - info["p"])


def ending_condition_function(history_data, info):
    return len(history_data) >= num_rounds or (len(history_data) != 0 and history_data[-1][3] <= 0)


game = GambleGame(bankroll, decision_function, gamble_function, ending_condition_function, info)

bankroll_history_of_different_games = []

for i in range(num_experiment):
    game.replay()

    bankroll_list = [x[0] for x in game.history_data] + [game.history_data[-1][3]]
    num_list = [x for x in range(len(bankroll_list))]

    if len(bankroll_list) < num_rounds:
        bankroll_list += [bankroll_list[-1]] * (num_rounds - len(bankroll_list) + 1)

    # print(bankroll_list)
    # print(len(bankroll_list))
    if game.info["id"] == 1:
        print("history of one game", game.history_data)

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

# calculate the wanted E[log(X+1)]

print("\n============\ncalculation & theoretical result:")
pi = info["p"] + (info["p"] - 1) / info["b"]
print("pi:", pi)

E = p * numpy.log(1 + pi * b) + q * numpy.log(1 - pi)
gr = numpy.exp(E) - 1

print("E:", E)
print("growth rate", gr)
print("expected value:", bankroll * ((gr + 1) ** num_rounds))

print("\n============\nexperiment result:")

print("actual mean value:", average_bankroll[-1])

actual_growth_rate = (average_bankroll[-1] / bankroll) ** (1 / num_rounds) - 1
print("actual mean growth rate:", actual_growth_rate)

# get the median of the results
final_bankroll = [x[-1] for x in bankroll_history_of_different_games]

median_bankroll = numpy.median(final_bankroll)
print("median bankroll:",median_bankroll)
median_growth_rate = (median_bankroll / bankroll) ** (1 / num_rounds) - 1
print("median growth rate:", median_growth_rate)
