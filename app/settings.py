import os
import time

os.environ['TZ'] = 'Europe/Madrid'
time.tzset()

status_api_url = os.environ['STATUS_API_URL']
discord_bot_token = os.environ['DISCORD_BOT_TOKEN']
discord_play_game = os.environ['DISCORD_PLAY_GAME']
discord_status_channel_id = int(os.environ['DISCORD_STATUS_CHANNEL_ID'])
discord_players_channel_id = int(os.environ['DISCORD_PLAYERS_CHANNEL_ID'])
