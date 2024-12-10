import telebot

bot = telebot.TeleBot('7470028860:AAGW5CoVl6VaOvP0wXlqeRWHIC3wH04Nei4')

@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    if message.text == "/start" or message.text == "Hello":
        bot.send_message(message.from_user.id, "Hi! I`m Dima! I am a Student Acadamy IT Step  from Belarus."
        "I'm a beginner programmer who really loves hedgehogs.\n"
        "In my free time, I playing mobily games and ride on the bike in summer.Here are some of my projects:\n"
        "- [Fufel prank](https://student162009.github.io/FUFELMEM/)\n"
        "- [Task list](https://student162009.github.io/Task-list/)\n"
        "- Task-list2.0 (not released)\n"
        "- [Relax player](https://student162009.github.io/Relax-player/)\n"
        "- [Flappy-Bird (Only PC) (P.S. To play, press the space bar)](https://student162009.github.io/Fluppy-Bird/)\n")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Write: /start or Hello")
    else:
        bot.send_message(message.from_user.id, "i dont understand :( /help.")

bot.polling(none_stop=True, interval=0)
