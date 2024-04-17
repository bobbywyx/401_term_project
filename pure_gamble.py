import random
import numpy
from matplotlib import pyplot as plt

# Gamble

# Parameters

# Initial Bankroll
bankroll = 1

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
    "num_rounds": num_rounds
}

print("game info:", info)
print("num_rounds:", num_rounds)


def gamble_function(money_in_bet, info):
    if random.random() < info["p"]:
        return (1 + info["b"]) * money_in_bet
    else:
        return 0


def decision_function(history_data, info):
    # return 0.1
    return info["p"] + (info["p"] - 1) / info["b"]
    # return (info["p"]*info["b"] + info["p"] -1) / (info["p"] * info["b"] * info["b"] + 1 - info["p"])


def ending_condition_function(history_data, info):
    return len(history_data) >= info["num_rounds"] or (len(history_data) != 0 and history_data[-1][3] <= 0)


def calc_plot(bankroll_history_of_different_games):
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

    average_bankroll = numpy.mean(bankroll_history_of_different_games, axis=0)
    print("actual mean value:", average_bankroll[-1])

    actual_growth_rate = (average_bankroll[-1] / bankroll) ** (1 / num_rounds) - 1
    print("actual mean growth rate:", actual_growth_rate)

    # get the median of the results and the index of the median
    final_bankroll = [x[-1] for x in bankroll_history_of_different_games]
    median_bankroll = numpy.median(final_bankroll)
    print("median bankroll:", median_bankroll)
    median_growth_rate = (median_bankroll / bankroll) ** (1 / num_rounds) - 1
    print("median growth rate:", median_growth_rate)

    median_index = final_bankroll.index(median_bankroll)
    print("median index:", median_index)

    # plot

    x = [x for x in range(len(bankroll_history_of_different_games[-1]))]

    fig, ax = plt.subplots()

    # for i in range(len(bankroll_history_of_different_games)):
    for i in range(20):
        ax.plot(x, bankroll_history_of_different_games[i], alpha=0.3)
        # ax.plot(x, (bankroll_history_of_different_games[i]), label='Data ' + str(i))

    # get the average of the bankroll history

    # print(average_bankroll)
    ax.plot(x, average_bankroll, label='Average', color='red', linestyle='--', linewidth=2)

    # draw the median line
    ax.plot(x, bankroll_history_of_different_games[median_index], color='blue', label='Median',
            linewidth=2)

    # q1,q3
    q1, q3 = numpy.percentile(final_bankroll, 25), numpy.percentile(final_bankroll, 75)
    q1_index, q3_index = final_bankroll.index(q1), final_bankroll.index(q3)
    print("q1:", q1)
    print("q1 index:", q1_index)
    print("q3:", q3)
    print("q3 index:", q3_index)

    ax.plot(x, bankroll_history_of_different_games[q1_index], color='green', label='Q1',
            linewidth=2)
    ax.plot(x, bankroll_history_of_different_games[q3_index], color='orange', label='Q3',
            linewidth=2)

    # y label
    ax.set_ylabel('log10(bankroll)')

    # y axis label
    ax.set_xlabel('rounds')
    ax.set_ylabel('log10(bankroll)')

    ax.set_yscale('log')

    ax.legend()

    ax.grid(True)

    # set the picture size
    fig.set_size_inches(10, 5)

    # set the title
    plt.title("p = %.1f, b = %.1f, $\pi$ = %.1f" % (p, b, pi))

    plt.savefig("figure2.png")
