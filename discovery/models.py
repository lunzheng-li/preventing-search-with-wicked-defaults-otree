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

    num_rounds = 80  # + 2  # TODO change this value based on debug, it seems that it's defined but never used
    num_rounds_to_pay = 4
    point_to_dollar_factor = 50  # this value exists in setting.py
    offers_bottom = 0  # exclusive
    offers_top = 100  # inclusive
    # cost_of_offer = 10

    instructions_template = 'discovery/Instructions_temp.html'


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.session.config.get("cost_of_offer") == 5:
            with open('discovery/draws005_seed1.json', encoding='utf-8') as f:
                rows = json.load(f)  # 30*800
        else:
            with open('discovery/draws03_seed1.json', encoding='utf-8') as f:
                rows = json.load(f)  # 30*800

        with open('discovery/default_sequence_seed1.json', encoding='utf-8') as f:
            defaults = json.load(f)
            # print(type(defaults))  # 1*80

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

            p.default_rounds = json.dumps(defaults)
            # print(p.default_rounds)
            # print(type(p.default_rounds))

            # let's first set initial optDefault
            # if subject click reveal button, the value is updated with live_next_payoff
            if defaults[self.round_number - 1] == 1:
                p.optDefault = 1
            else:
                p.optDefault = 2


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # participant information
    participant_name = models.StringField()
    participant_signature = models.StringField()
    participant_date = models.StringField()
    # game information
    num_cards = models.IntegerField()
    cost_of_offer = models.IntegerField()
    default_rounds = models.StringField()
    numbers = models.StringField()
    optDefault = models.IntegerField()

    index_revealed = models.IntegerField(initial=1)

    # add an optDefault var

    def live_next_payoff(self, data):
        # see what you have access to here
        self.index_revealed = data[0]
        self.optDefault = data[1]
        return {self.id_in_group: self.index_revealed}
    # seems that the live method may depend on the Internet speed.
    index_revealed_check = models.IntegerField(initial=1)

    round_payoff = models.IntegerField(initial=0)
    round_best_offer = models.IntegerField()
    round_cost_of_offers = models.IntegerField()

    comp_best_offer = models.IntegerField(
        label="What is the best offer so far?"
    )
    comp_cost_of_offers = models.IntegerField(
        label="What is the cost of offers if you accept the best offer?"
    )
    comp_payoff = models.IntegerField(
        label="What is your payoff if you accept the best offer?"
    )

    chosen_rounds = models.StringField()
    total_payoff = models.IntegerField()
    pay_id = models.StringField()
    confirm_pay_id = models.StringField()
