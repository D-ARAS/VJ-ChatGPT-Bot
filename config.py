import re
from os import getenv, environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

API_ID = int(environ.get("API_ID", "1067319"))
API_HASH = environ.get("API_HASH", "147745612b97af716648f754d6232a1e")
BOT_TOKEN = environ.get("BOT_TOKEN", "6159878431:AAHjLaDDdPK76ePyW259-Ypcs4HRIE3kC-E")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002071052995"))
ADMINS = int(environ.get("ADMINS", "1017109568"))
DB_URI = environ.get("DB_URI", "mongodb+srv://ifpdftp:x)Oi0a!V1Q414@cluster0.eyxxb26.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "chatgptvjbot")
OPENAI_API = environ.get("OPENAI_API", "")
AI = is_enabled((environ.get("AI","True")), False)
