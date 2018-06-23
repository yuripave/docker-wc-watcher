import os

WEBHOOK_URL = os.getenv('WEBHOOK_URL') # Slack webhook
DEBUG_WEBHOOK = os.getenv('DEBUG_WEBHOOK') # Webhook for sending debug information
DEBUG = False
if os.getenv('DEBUG'):
    DEBUG = True

# Use to override default webhook messaging settings
BOT_NAME = os.getenv('BOT_NAME', 'WorldCup-Bot') # Bots username
ICON_EMOJI = os.getenv('ICON_EMOJI', ':soccer:') # Bots Avatar
CHANNEL = os.getenv('CHANNEL') # Channel to send messages to. Ex: 'random'
DEBUG_CHANNEL = os.getenv('DEBUG_CHANNEL')# Channel to send debug messages
