from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import json


class One(Page):
    form_model = "player"

    form_fields = [
        "last_offer",
        "highest_offer",
        "num_offers",
        "earnings_greater",
        "offer_smaller",
        "highest_offer",
        "other_reason"
    ]
    def error_message(self, values):
        if all(x is None for x in values.values()):
            return "You have to answer atleast one question"

class Two(Page):
    form_model = "player"

    form_fields = [
        "two_one", "two_two", # "two_three"
    ]
    def vars_for_template(self):
        return dict(
            cost_of_offer=self.session.config.get('cost_of_offer'),
        )

page_sequence = [
    One,
    Two,
]
