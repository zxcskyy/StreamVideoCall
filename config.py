# Copyright (C) 2021 By VeezMusicProject

import os
from os import path, getenv
from dotenv import load_dotenv

if path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()

class Woof(object):
        admins = {}
        BOT_TOKEN = getenv("BOT_TOKEN", None)
        CHANNEL = int(os.getenv('CHANNEL', 1403131105))
        API_ID = int(getenv("API_ID", "8752359"))
        API_HASH = getenv("API_HASH", "53b80a9ea6353a10d510469efbc8555d")
        SESSION_NAME = getenv("SESSION_NAME", None)
        DURATION_LIMIT = int(getenv("DURATION_LIMIT", "9999"))
        SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
        ASSISTANT_NAME = getenv("ASSISTANT_NAME", "woofiemusicvideoassistant")
        BOT_USERNAME = getenv("BOT_USERNAME", "mailmusicupdate")
        COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
        CHANNEL_NAME = getenv("CHANNEL_NAME", "mailmusicupdate")
        GROUP_NAME = getenv("GROUP_NAME", "mailmusicupdate")
        OWNER_NAME = getenv("OWNER_NAME", "ner")
