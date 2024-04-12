import random
import numpy
import math
import matplotlib.pyplot as plt

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


while num_rounds <= 100 and bankroll > 0:
    # Kelly's criterion
    proportion = p + (p - 1) / b
    # Bet size
    Y0 = proportion * bankroll

    if random.random() < p:  # Win
        Y1 = (1 + b) * Y0
    else:                   # Lose
        Y1 = 0

    bankroll = bankroll - Y0 + Y1
    num_rounds += 1
    num_list.append(num_rounds)
    bankroll_list.append(bankroll)


# plt.title("Simulation of Kelly Criterion")

plt.subplot(1, 2, 1)
plt.plot(num_list, bankroll_list)
plt.xlabel("n")
plt.ylabel("Bankroll")

plt.subplot(1, 2, 2)
plt.plot(num_list, numpy.log10(bankroll_list))
plt.xlabel("n")
plt.ylabel("Bankroll (log scale)")
plt.savefig("figure.png")
