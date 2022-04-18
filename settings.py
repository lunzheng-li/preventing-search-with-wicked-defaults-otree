from os import environ

SESSION_CONFIGS = [
    dict(
        name="two_treatments",
        display_name="Search Cost - please set cost_of_offer in Configure session",
        num_demo_participants=1,  # default
        # discovery parameters
        num_rounds=10,  # used
        cost_of_offer=5,  # used


        # debug=debug,

        num_cards=10,  # used
        endowment=200,  # used
        point_to_dollar_factor=50,  # used


        # seems that the following are the parameters for wicked
        only_pay_single_round=True,
        aversion_win=2.00,
        aversion_multiplier=0.1,
        num_trial_rounds=1,
        small_grids=12,
        middle_grids=0,
        large_grids=0,
        small_grids_order=1,
        middle_grids_order=2,
        large_grids_order=3,
        num_insurance_colours=4,
        num_selected_insurance_default=4,
        num_selected_insurance_default_trial=4,
        probability_red=18,
        probability_orange=18,
        probability_yellow=14,
        probability_green=13,
        probability_blue=0,
        probability_purple=0,
        probability_pink=0,
        low_info_multiplier=10,
        medium_info_multiplier=4,
        high_info_multiplier=2,
        full_info_multiplier=1,
        price_floor=12,
        loss_amount=100,
        task_trial_timeout_seconds=60,
        task_timeout_seconds=45,
        seed=18,
        enable_skip=False,
        x_tokens_per_1_aud=10,
        app_sequence=[
            "discovery",
            "questionnaire",
            # "wicked_defaults_optimal",
        ],
    ),
    dict(
        name='show_up',
        display_name="Show Up",
        num_demo_participants=1,
        app_sequence=['show_up'],
        show_up_fee=5.00,
    ),

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.02, participation_fee=5.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'AUD'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '!%3nc_4*fpge%5so8)d(ek1ck8e-69tm8a#$*^q5!st-^yye71'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
