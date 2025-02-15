import pyrogram
import os

api_id = 29992800
api_hash = "cc89e649f8bb0f78bc7b03fc582dcd30"

print(api_id)
print(api_hash)


app = pyrogram.Client(name="LoadVideoWithCover", no_updates=False, sleep_threshold=10, api_id=api_id,
                          api_hash=api_hash)


async def main():
    async with app:
    # messages = await app.get_messages(chat_id="me", message_ids=20)
    #
    # for message in messages:
    #     print(message)
    # "me" refers to your own chat (Saved Messages)
    #     async for message in app.get_chat_history("me"):
    #         print(message)
        my_emoji_str = "<emoji id=5307817835341298185>🌟</emoji>"
        await app.send_message("avetoshkina", my_emoji_str)

app.run(main())