import telebot
bot = telebot.TeleBot('5222695046:AAHFQKLX_qYqE3kKcqSEbe4Sxc6uhSgPx-k')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "������":
      bot.send_message(message.from_user.id, "������! ��� � ���� ���� ������?")
      bot.send_message(message.from_user.id, "��������� �������:\n����������\n���������\n����")
      bot.send_message(message.from_user.id, "�� ������� /help ���� ����� �������� ���� ������")
  elif message.text == "/help":
      bot.send_message(message.from_user.id, "��������� �������:\n����������\n���������\n����")
  else:
      bot.send_message(message.from_user.id, "� ���� �� �������. ������ /help.")

bot.polling(none_stop=True, interval=0) #����������� ������ ����� ���������
