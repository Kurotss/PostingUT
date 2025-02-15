import telebot
import os
token=os.getenv("TOKEN")
chat_id_user_bot = os.getenv("CHAT_ID_USER_BOT")
bot=telebot.TeleBot(token)

@bot.message_handler(content_types = ['text', 'video'])
def message_text(message):
     bot.send_video(chat_id = chat_id_user_bot,
                        video = message.video.file_id,
                        caption = message.caption)

bot.infinity_polling()