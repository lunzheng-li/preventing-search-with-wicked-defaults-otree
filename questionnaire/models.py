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

author = "Your name here"

doc = """
Your app description
"""


class Constants(BaseConstants):
    players_per_group = None
    name_in_url = "questionnarie"
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    last_offer = models.IntegerField(
        label="A: If the last offer is greater than or equal to ",
        blank=True
    )
    highest_offer = models.IntegerField(
        label="B: If the highest offer is greater than or equal to ",
        blank=True
    )
    num_offers = models.IntegerField(
        label="C: If the number of offers revealed so far is greater than or equal to ",
        blank=True
    )
    earnings_greater = models.IntegerField(
        label="D: If my earnings are greater than or equal to",
        blank=True
    )
    offer_smaller = models.IntegerField(
        label="E: If _____ offers in a row are smaller than the highest offer so far",
        blank=True
    )
    other_reason = models.StringField(label="F: Other", blank=True)
    # questionnarie 2
    two_one = models.IntegerField(
        label="1.   Suppose you choose to pay XX points to reveal another offer. You then learn that the new offer turns out to be no better than the current best offer. Please rate the intensity of the regret you anticipate experiencing in this situation (tick one box below):",
        # TODO logic needs to be a bit different if we need to include text labels.
        choices=[[x, x] for x in range(1, 10)],
        widget=widgets.RadioSelect,
    )
    two_two = models.IntegerField(
        label="2.   Suppose you choose to accept the current best offer. You then learn that the next offer on the list could have been better than the current best offer. Please rate the intensity of the regret you anticipate experiencing in this situation (tick one box below):",
        choices=[[x, x] for x in range(1, 10)],
        widget=widgets.RadioSelect,
    )
    # two_three = models.IntegerField(
    #     label="3. Suppose you choose to accept the current best offer. Like in the experiment, you do not learn about the other offers. Please rate the intensity of the regret you anticipate experiencing in this situation (tick one box below):",
    #     choices=[[x, x] for x in range(1, 10)],
    #     widget=widgets.RadioSelect,
    # )
