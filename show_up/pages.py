from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ParticipationPage(Page):
    pass


class Consent(Page):
    form_model = 'player'
    form_fields = ['participant_name',
                   'participant_signature', 'participant_date']


class Summary(Page):
    form_model = 'player'
    form_fields = ['pay_ID', 'pay_ID_check']

    def error_message(self, values):
        if values['pay_ID'] != values['pay_ID_check']:
            return 'The second PayID must match the first!'


class Thankyou(Page):
    pass


page_sequence = [
    ParticipationPage,
    Consent,
    Summary,
    Thankyou
]
