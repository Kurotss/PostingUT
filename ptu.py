import pyrogram
import argparse
import os.path
import hachoir.parser
import hachoir.metadata
from PIL import Image
from resizeimage import resizeimage
import tempfile
import sys
from datetime import datetime
from PIL import Image
from input_descr import *
import re

## F:\pervayazvezda.mp4
## F:\Обложка на видео.jpg

def upload_progress(cur, max):
    print("upload:" + str(round(100 * cur / max, 2)), flush=True)

api_id = 29992800
api_hash = "cc89e649f8bb0f78bc7b03fc582dcd30"

video_path, thumb_path, schedule_date_string = enter_video_info()

try:
    datetime.strptime(schedule_date_string,"%Y-%m-%d %H:%M" )
    
except ValueError:
    print("Дата не соответствует формату yyyy-mm-dd HH:MM")
    sys.exit()
    
info = None
with open(video_path, 'rb') as f:
    info = hachoir.metadata.extractMetadata(hachoir.parser.createParser(video_path))
    
with Image.open(thumb_path) as img:
    width, height = img.size

if thumb_path is not None and os.path.exists(thumb_path) and os.path.isfile(thumb_path):
    tmp = tempfile.mkstemp(prefix="TGU")[1] + ".jpg"
    with open(thumb_path, 'r+b') as f:
        with Image.open(f) as image:
            image = image.convert("RGB")
            cover = resizeimage.resize_cover(image, [256,144], validate=False)
            cover.save(tmp, 'jpeg', quality=100, smooth=True)
            thumb_path = tmp

message = make_description()
message += f'{schedule_date_string}'

#open telegram
client = pyrogram.Client(name ="LoadVideoWithCover", no_updates=True, sleep_threshold=10, api_id = api_id, api_hash = api_hash)
client.start()
##

video = None
thumb = None

if video_path is not None and os.path.exists(video_path) and os.path.isfile(video_path):
    print("Загрузка видео на телеграм-сервер")
    video = client.save_file(path=video_path, progress=upload_progress)
    print("Видео успешно загружено на телеграм-сервер")

if thumb_path is not None and os.path.exists(thumb_path) and os.path.isfile(thumb_path):
    thumb = client.save_file(thumb_path)

print("Отправка видео телеграм-боту")
msg = client.invoke(pyrogram.raw.functions.messages.SendMedia(
    peer=client.resolve_peer("mottopost"),
    media= pyrogram.raw.types.InputMediaUploadedDocument(
        mime_type="video/mp4",
        file=video,
        attributes=[
            pyrogram.raw.types.DocumentAttributeVideo(
                supports_streaming=True,
                duration=info.get('duration').seconds,
                w=width,
                h=height
            ),
            pyrogram.raw.types.DocumentAttributeFilename(file_name=video.name),
        ],
        thumb=thumb
    ),
    random_id=client.rnd_id(),
    silent=None,
    reply_to_msg_id=None,
    message=message
))
print("Видео успешно отправлено телеграм-боту")

os.remove(thumb_path)
client.stop()
print("finish:0", flush=True)
input()
