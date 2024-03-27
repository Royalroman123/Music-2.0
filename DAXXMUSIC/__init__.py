from DAXXMUSIC.core.bot import DAXX
from DAXXMUSIC.core.dir import dirr
from DAXXMUSIC.core.git import git
from DAXXMUSIC.core.userbot import Userbot
from DAXXMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = DAXX()
api = SafoneAPI()
userbot = Userbot()

DRAGONS = get_user_list("elevated_users.json", "sudos")  # DON'T EDIT
DEV_USERS = get_user_list("elevated_users.json", "devs")  # . DON'T EDIT
DEMONS = get_user_list("elevated_users.json", "supports")  # DON'T EDIT
WOLVES = get_user_list("elevated_users.json", "whitelists")  # DON'T EDIT
TIGERS = get_user_list("elevated_users.json", "tigers")  # DON'T EDIT


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
