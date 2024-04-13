class GambleGame:
    # store info
    initial_money = 100
    current_money = 0

    # each element is a tuple (money_before_bet, money_in_bet, round_result, money_after_bet)
    # e.g. [(100, 10, 30, 120), (120, 80, -80, 40), ...]
    history_data = []

    # other required info
    info = {
        "id": 0,
    }

    # function pointers

    # this function should return a float value, which is the proportion of current money to bet
    decision_function = None

    # this function should return a float value, which is the result of the gamble, positive for win, negative for lose
    # e.g. 10 for win 10, -20 for lose 20
    gamble_function = None

    # this function should return a bool value, which is the ending condition of the game, ture for ending
    ending_condition_function = None

    # constructor
    def __init__(self, initial_money, decision_function, gamble_function, ending_condition_function, info):
        self.initial_money = initial_money
        self.current_money = initial_money
        self.decision_function = decision_function
        self.gamble_function = gamble_function
        self.ending_condition_function = ending_condition_function
        self.info = info

    def play_one_round(self):
        proportion = self.decision_function(self.history_data, self.info)
        money_in_bet = proportion * self.current_money
        round_result = self.gamble_function(money_in_bet, self.info)
        money_after_bet = self.current_money - money_in_bet + round_result
        self.history_data.append((self.current_money, money_in_bet, round_result, money_after_bet))
        self.current_money = money_after_bet
        return round_result

    def play(self):
        print("Game start!")
        while not self.ending_condition_function(self.history_data, self.info):
            round_result = self.play_one_round()
            print("== round %d ==" % len(self.history_data))
            print("Round result: ", round_result)
            print("Current money: ", self.current_money)
        print("Game end!")