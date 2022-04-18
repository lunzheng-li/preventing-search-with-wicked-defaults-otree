from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import json
import random

author = "Ishaan Varshney & Lunzheng Li"

doc = """
To do list:
1. (done)put instructions below
2. (done)make the Page display similar to sample screenshot in instruction.
3. (be careful...)delete unnessary vars in setting - they are part of wicked games
4. (done)check that the instructions are right.
5. (done)The show up fee app.
6. check for different rounds and different subjects.

15-Apr, let me first put eveything online and send to Zhang.
"""


class Constants(BaseConstants):
    name_in_url = "discovery"
    players_per_group = None
    # TODO make this a high number and then cut it off depending on
    # settings.py https://otree.readthedocs.io/en/self/rounds.html?highlight=num_rounds#variable-number-of-rounds
    num_rounds = 80  # + 2  # TODO change this value based on debug
    num_rounds_to_pay = 4
    point_to_dollar_factor = 50  # this value exists in setting.py
    offers_bottom = 0  # exclusive
    offers_top = 100  # inclusive
    # cost_of_offer = 10

    instructions_template = 'discovery/Instructions_temp.html'


class Subsession(BaseSubsession):
    def creating_session(self):
        with open('discovery/draws.json', encoding='utf-8') as f:
            rows = json.load(f)  # 30*800
        for ind, p in enumerate(self.get_players()):

            p.num_cards = self.session.config.get("num_cards")
            p.cost_of_offer = self.session.config.get("cost_of_offer")

            # every subject has 800 random numbers and it's decide at the begining
            # which is dump into a json file.
            p.numbers = json.dumps([round(x * 100) for x in rows[ind]])

            rounds_to_pay = sorted(
                random.sample(
                    range(1, self.session.config.get('num_rounds') + 1),
                    Constants.num_rounds_to_pay,
                )
            )
            p.participant.vars["chosen_rounds"] = json.dumps(
                {x: 0 for x in rounds_to_pay}
            )


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    index_revealed = models.IntegerField(initial=1)
    num_cards = models.IntegerField()
    cost_of_offer = models.IntegerField()

    def live_next_payoff(self, data):
        # see what you have access to here
        self.index_revealed = data

    chosen_rounds = models.StringField()
    # this needs to be refreshed per subsession (aka round)
    numbers = models.StringField()
    round_payoff = models.IntegerField(initial=0)
    comp_best_offer = models.IntegerField(
        label="What is the best offer so far?"
    )
    comp_cost_of_offers = models.IntegerField(
        label="What is the cost of offers if you accept the best offer?"
    )
    comp_payoff = models.IntegerField(
        label="What is your payoff if you accept the best offer?"
    )
    total_payoff = models.IntegerField()
    pay_id = models.StringField()
    confirm_pay_id = models.StringField()
