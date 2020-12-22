from gitbot import Bot

bot = Bot.github("LinkerScript", "pogger1A", delay=0)

while True:
    bot.unlimited_commits()
