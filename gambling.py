import random
import numpy
import math
import matplotlib.pyplot as plt

import gamble_with_uncertantiy as rule
from game_class import GambleGame

num_experiment = 501

game = GambleGame(rule.bankroll, rule.decision_function, rule.gamble_function,
                  rule.ending_condition_function, rule.info)

bankroll_history_of_different_games = []

num_rounds = rule.num_rounds

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

rule.calc_plot(bankroll_history_of_different_games)
