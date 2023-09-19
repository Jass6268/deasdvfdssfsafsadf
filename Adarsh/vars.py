# (c) adarsh-goel

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(15037283)
    API_HASH = str("7af9d761267bf6b81ed07f942d87127f")
    BOT_TOKEN = str("6685706580:AAHkEePNy21IsAJ0sTLE_2EKh0D9qNU_0WY")
    SESSION_NAME = str(getenv('SESSION_NAME', 'MCFILESTREAMER'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(-1001645923712)
    PORT = int(getenv('PORT', 5000))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', 'marvelcloud.starkai.live'))
    OWNER_ID = int(getenv('OWNER_ID', '2043144248'))
    NO_PORT = bool(getenv('NO_PORT', True))
    APP_NAME = None
    OWNER_USERNAME = str("MarvelCloud")
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
        "http://{}:{}/".format(FQDN, PORT)
    DATABASE_URL = str("mongodb+srv://stark:stark@cluster0.9sxyrqb.mongodb.net/")
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split()))
