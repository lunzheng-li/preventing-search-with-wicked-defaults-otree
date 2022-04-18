from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random
import json


class ParticipationPage(Page):
    def is_displayed(self):
        return self.round_number == 1


class Consent(Page):
    form_model = "player"

    def is_displayed(self):
        return self.round_number == 1


class Comprehension(Page):
    form_model = "player"

    form_fields = ["comp_best_offer", "comp_cost_of_offers", "comp_payoff"]

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return dict(
            cost_of_offer=self.player.cost_of_offer,
            numbers=[74, 25, 61, 40, 1, 1, 1, 1, 1, 1],
            index_values=list(range(self.player.num_cards)),
            round_number=self.round_number,
            number_of_rounds=self.session.config.get('num_rounds'),
            index_revealed=4,
        )

    def error_message(self, values):
        solutions = dict(
            comp_best_offer=(
                74,
                "The best offer will be the one highlighted in yellow",
            ),
            comp_cost_of_offers=(
                3 * self.player.cost_of_offer,
                f"Each reveal costs {self.player.cost_of_offer} points",
            ),
            comp_payoff=(
                self.session.config.get('endowment') +
                74 - 3 * self.player.cost_of_offer,
                "The payoff is the endowment (200) + best payoff - the costs so far",
            ),
        )
        error_messages = dict()

        for field_name in solutions:
            if values[field_name] != solutions[field_name][0]:
                error_messages[field_name] = solutions[field_name][1]

        return error_messages


class Instructions(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return dict(
            participation_fee=int(self.session.config["participation_fee"]),
            num_rounds=self.session.config.get('num_rounds'),
            num_cards=self.player.num_cards,
            num_cards_minus_1=self.player.num_cards - 1,
            num_rounds_to_pay=Constants.num_rounds_to_pay,
            point_to_dollar_factor=self.session.config.get(
                'point_to_dollar_factor'),
            endowment=self.session.config.get('endowment'),
            offers_bottom=Constants.offers_bottom,
            offers_top=Constants.offers_top,
            cost_of_offer=self.player.cost_of_offer,
        )


class Game(Page):
    form_model = "player"
    live_method = "live_next_payoff"

    form_fields = ["round_payoff"]

    def vars_for_template(self):
        numbers = json.loads(self.player.numbers)
        curr_round_numbs = numbers[(
            self.round_number - 1) * 10:self.round_number * 10]
        return dict(
            participation_fee=int(self.session.config["participation_fee"]),
            num_rounds=self.session.config.get('num_rounds'),
            num_rounds_to_pay=Constants.num_rounds_to_pay,
            point_to_dollar_factor=self.session.config.get(
                'point_to_dollar_factor'),
            endowment=self.session.config.get('endowment'),
            num_cards=self.player.num_cards,
            num_cards_minus_1=self.player.num_cards - 1,
            offers_bottom=Constants.offers_bottom,
            offers_top=Constants.offers_top,
            cost_of_offer=self.player.cost_of_offer,
            numbers=curr_round_numbs,
            index_values=list(range(self.player.num_cards)),
            round_number=self.round_number,
            number_of_rounds=self.session.config.get('num_rounds'),
            index_revealed=self.player.index_revealed,
        )

    def before_next_page(self):
        chosen_rounds = json.loads(
            self.player.participant.vars["chosen_rounds"]
        )
        round_number = str(self.player.round_number)
        if round_number in chosen_rounds:
            chosen_rounds[round_number] = self.player.round_payoff
            self.player.participant.vars["chosen_rounds"] = json.dumps(
                chosen_rounds
            )

    def app_after_this_page(self, upcoming_apps):
        if self.round_number == self.session.config.get('num_rounds'):
            rounds_payoffs = json.loads(
                self.player.participant.vars["chosen_rounds"]
            )
            payoff = sum(rounds_payoffs.values())
            self.player.total_payoff = payoff + \
                len(rounds_payoffs) * self.session.config.get("endowment")
            self.player.participant.vars["game_total_payoff"] = self.player.total_payoff
            self.player.payoff = self.player.total_payoff / \
                self.session.config.get('point_to_dollar_factor')
            return upcoming_apps[0]


class Summary(Page):
    form_model = "player"
    form_fields = ["pay_id", "confirm_pay_id"]

    def is_displayed(self):
        return self.round_number == self.session.config.get('num_rounds')

    def vars_for_template(self):
        rounds_payoffs = json.loads(
            self.player.participant.vars["chosen_rounds"]
        )
        total_payoff = sum(rounds_payoffs.values())
        self.player.total_payoff = total_payoff + \
            len(rounds_payoffs) * self.session.config.get("endowment")
        self.player.payoff = total_payoff / \
            self.session.config.get('point_to_dollar_factor')
        return dict(
            total_payoff=self.player.total_payoff,
            chosen_rounds=", ".join(rounds_payoffs.keys()),
            rounds_payoffs=rounds_payoffs.items(),
        )

    def before_next_page(self):
        rounds_payoffs = json.loads(
            self.player.participant.vars["chosen_rounds"]
        )
        payoff = sum(rounds_payoffs.values())
        self.player.total_payoff = payoff + \
            len(rounds_payoffs) * self.session.config.get("endowment")
        self.player.participant.vars["game_total_payoff"] = self.player.total_payoff
        self.player.payoff = self.player.total_payoff / \
            self.session.config.get('point_to_dollar_factor')

    def error_message(self, values):
        if values['pay_id'] != values['confirm_pay_id']:
            return "The pay id values do not match"

    def app_after_this_page(self, upcoming_apps):
        return upcoming_apps[0]


class PostResults(Page):
    form_model = "player"

    def is_displayed(self):
        return self.round_number == self.session.config.get('num_rounds')

    def app_after_this_page(self, upcoming_apps):
        # if you have reached the summary we need to move
        # onto the next app
        return upcoming_apps[0]


page_sequence = [
    ParticipationPage,
    Consent,
    Instructions,
    Comprehension,
    Game,
    # seems that the following two page does not matter, figure out why?
    # Summary,
    # PostResults,
]
