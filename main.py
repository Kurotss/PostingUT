from datetime import datetime
import pyrogram
import os

chat_id = os.getenv("CHAT_ID")
api_id = os.getenv("api_id")
api_hash = os.getenv("API_HASH")
phone_number =os.getenv("PHONE_NUMBER")

app = pyrogram.Client(name="LoadVideoWithCover", no_updates=False, sleep_threshold=10, api_id=api_id,
                          api_hash=api_hash, phone_number=phone_number)

@app.on_message()
async def my_handler(client, message):
     message_rows = str(message.caption).split('\n')
     schedule_date = datetime.strptime(message_rows[-1],"%Y-%m-%d %H:%M" )
     caption = '\n'.join(message_rows[:-1])
     await app.send_video(
         chat_id = chat_id,
         video = message.video.file_id,
         caption = caption,
         schedule_date = schedule_date
     )

app.run()


#bot.polling(none_stop=True, interval=0)
