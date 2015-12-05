from gitbot import Bot
import os

# Set environment variables

PASSWORD = os.environ.get('API_PASSWORD')
bot = Bot.github("LinkerScript", PASSWORD, delay=0)

while True:
    bot.unlimited_commits()
