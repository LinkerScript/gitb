from gitbot import Bot

bot = Bot.github("LinkerScript", "", delay=0)

while True:
    bot.unlimited_commits()
