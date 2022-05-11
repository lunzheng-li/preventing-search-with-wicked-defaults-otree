from os import environ

SESSION_CONFIGS = [
    dict(
        name="two_treatments",
        display_name="Search Cost - no info",
        num_demo_participants=1,  # default
        # discovery parameters
        num_rounds=10,  # used
        cost_of_offer=5,  # used

        num_cards=10,  # used
        endowment=200,  # used
        point_to_dollar_factor=100,  # used


        app_sequence=[
            "discovery",
            "questionnaire",
            "risk_quiz",
        ],
    ),
    dict(
        name="two_treatments_info",
        display_name="Search Cost - with info",
        num_demo_participants=1,  # default
        # discovery parameters
        num_rounds=10,  # used
        cost_of_offer=5,  # used

        num_cards=10,  # used
        endowment=200,  # used
        point_to_dollar_factor=100,  # used


        app_sequence=[
            "discovery_info",
            "questionnaire",
            "risk_quiz",
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
    real_world_currency_per_point=0.01, participation_fee=5.00, doc=""
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
