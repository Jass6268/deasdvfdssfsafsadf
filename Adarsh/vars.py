# (c) adarsh-goel

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(5390465)
    API_HASH = str("abafb7520db145a9157b09c066f9a399")
    BOT_TOKEN = str("6049118328:AAFNM4tTdktPFI98tIUt9anCVSDTIxbnGBI")
    SESSION_NAME = str(getenv('SESSION_NAME', 'HBSTREAMBOT'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(-1001696981337)
    PORT = int(getenv('PORT', 5000))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', ''))
    OWNER_ID = int(getenv('OWNER_ID', '1875452714'))
    NO_PORT = bool(getenv('NO_PORT', True))
    APP_NAME = None
    OWNER_USERNAME = str("HBMoviesGod")
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
        "http://{}:{}/".format(FQDN, PORT)
    DATABASE_URL = str("mongodb+srv://123:123@cluster0.f5pm3sh.mongodb.net/")
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001696981337")).split()))
