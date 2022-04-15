import telebot
bot = telebot.TeleBot('5222695046:AAHFQKLX_qYqE3kKcqSEbe4Sxc6uhSgPx-k')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "Привет":
      bot.send_message(message.from_user.id, "Привет! чем я могу тебе помочь?")
      bot.send_message(message.from_user.id, "Доступные команды:\nРасписание\nШпаргалки\nМемы")
      bot.send_message(message.from_user.id, "По нажатию /help тебе будет доступно меню команд")
  elif message.text == "/help":
      bot.send_message(message.from_user.id, "Доступные команды:\nРасписание\nШпаргалки\nМемы")
  else:
      bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0) #непрерывный запрос новых сообщений
