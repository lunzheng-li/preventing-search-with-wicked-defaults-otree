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


author = 'Lunzheng Li'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'show_up'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.payoff_showup = self.session.config['show_up_fee']

    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    participant_name = models.StringField()
    participant_signature = models.StringField()
    participant_date = models.StringField()
    # pay_ID
    pay_ID = models.StringField(
        label='Please enter your PayID (your PayID is either your email or your phone number):')

    pay_ID_check = models.StringField(
        label='Please re-enter your PayID :')

    payoff_showup = models.FloatField()
    pass
