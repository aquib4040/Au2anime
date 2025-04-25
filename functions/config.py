#    This file is part of the AutoAnime distribution.
#    Copyright (c) 2025 Kaif_00z
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/kaif-00z/AutoAnimeBot/blob/main/LICENSE > .

# if you are using this following code then don't forgot to give proper
# credit to t.me/kAiF_00z (github.com/kaif-00z)

from decouple import config


class Var:
    # Version

    __version__ = "v0.0.8"

    # Telegram Credentials

    API_ID = config("API_ID", default=20697474, cast=int)
    API_HASH = config("API_HASH", default="1acf41c146d578a57741ab0760208eb4")
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    SESSION = config("SESSION", default=1BVtsOJIBu1R-aBGfoFN0IenJWiFsYAVRh-m0dIQyF7gX-43W-YPOQSFcaaKF-2vZZAohDtoXv-CkXaOE3st2XXKAqZI_HkPRwThYb8tT2JrrBAoblP19dQNp-GsHB2-fEenEP0slAw_h7odKq1eEtMsQRADio6sThwH3e3QLsM-4991cEDiqH1gh-TY7ntRVFz1g9cTK-sJA2ZyMVCGFMeFG6JMnBx104b9lPYqE36UcBym5pbHNY_b-Q0VSEntCU3hO1SCl6pQK76_kHU-YL1jhU9mXoitxp7OVHfIf5FwKshHgSJtW507MLvLyfGx1XE7NQvsxMSX92JwYC5YOY3C5QUUhhfE=)

    # Database Credentials

    MONGO_SRV = config("MONGO_SRV", default=None)

    # Channels Ids

    BACKUP_CHANNEL = config("BACKUP_CHANNEL", default=-1002640759147, cast=int)
    MAIN_CHANNEL = config("MAIN_CHANNEL", default=-1002665222825, cast=int)
    LOG_CHANNEL = config("LOG_CHANNEL", default=-1002307383070,  cast=int)
    CLOUD_CHANNEL = config("CLOUD_CHANNEL", default=-1002239947544, cast=int)
    FORCESUB_CHANNEL = config("FORCESUB_CHANNEL", default=-1002201055953, cast=int)
    OWNER = config("OWNER", default=5851158054, cast=int)

    # Other Configs

    THUMB = config(
        "THUMBNAIL", default="https://i.ibb.co/zWRXXrgp/IMG-20250424-133644-397.jpg"
    )
    FFMPEG = config("FFMPEG", default="aquib")
    CRF = config("CRF", default="45")
    SEND_SCHEDULE = config("SEND_SCHEDULE", default=True, cast=bool)
    RESTART_EVERDAY = config("RESTART_EVERDAY", default=True, cast=bool)
    LOG_ON_MAIN = config("LOG_ON_MAIN", default=True, cast=bool)
    FORCESUB_CHANNEL_LINK = config("FORCESUB_CHANNEL_LINK", default="https://t.me/+2aWo_vvo3d44MjA1", cast=str)

    # Dev Configs

    DEV_MODE = config("DEV_MODE", default=True, cast=bool)
