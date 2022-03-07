from . import CONFIG


# ---DB---#
DATABASE_URL = f'postgresql+psycopg2://{CONFIG["DB"]["DB_USER"]}:{CONFIG["DB"]["DB_PASS"]}' \
               f'@{CONFIG["DB"]["DB_HOST"]}:{CONFIG["DB"]["DB_PORT"]}/{CONFIG["DB"]["DB_NAME"]}'

# ---MOSMETRO---#
MOSMETRO_NEWS_URL = CONFIG["MOSMETRO"]["NEWS_URL"]

