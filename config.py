import ast
from os import environ
from pyrogram import filters


API_ID = environ.get('API_ID') # Get these two from https://my.telegram.org eg:1775946
API_HASH = environ.get('API_HASH') # Get these two from https://my.telegram.org.  eg:886c1579af458622eb3e20b6558d0337
TOKEN = environ.get('TOKEN')   ## Get this from @Botfather eg:1381605100:AAHrHbeA370bqjoar2VxC7jc1PM8II6nx8A
SUDO_USERS = environ.get('SUDO_USERS') # The IDs of the users which can stream, skip, pause and change volume. eg: 1116928578
GROUP = environ.get('GROUP') # The ID of the group where your bot streams. eg:-1001490179318
MONGO_DB_URI = environ.get('MONGO_DB_URI') # Your mongodb uri. eg:mongodb+srv://oxy_1709:yashi1709oxy@cluster0.8gtu0.mongodb.net/test?retryWrites=true&w=majority
USERS_MUST_JOIN = environ.get('USERS_MUST_JOIN', 'False') # Users must join the group before using the bot (note: the bot should be admin in the group if you enable this)
LANG = environ.get('LANG', 'en') # Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
DUR_LIMIT = environ.get('DUR_LIMIT', 10) # Max video duration allowed for user downloads in minutes




## No need to touch the following.
API_ID = int(API_ID)
SUDO_USERS = list(map(int, SUDO_USERS.split()))
if type(GROUP) is str:
  GROUP = int(GROUP)
DUR_LIMIT = int(DUR_LIMIT)
USERS_MUST_JOIN = ast.literal_eval(USERS_MUST_JOIN)
LOG_GROUP = GROUP if MONGO_DB_URI != "" else None
SUDO_FILTER = filters.user(SUDO_USERS)
