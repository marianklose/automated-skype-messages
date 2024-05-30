# type: ignore
# flake8: noqa
#
#
import random
import requests
from pathlib import Path
from openai import OpenAI
from skpy import Skype
from my_secrets import sk_username, sk_password
from my_secrets import OPENAI_KEY

# Initialize OpenAI API key
client = OpenAI(
    api_key = OPENAI_KEY
)

# connect to skype
sk = Skype(sk_username, sk_password)
#
#
#
# define the file path
speech_file_path = Path(__file__).parent / "speech.mp3"

# prompt
response = client.audio.speech.create(
  model="tts-1-hd",
  voice="alloy",
  input="Hey Davihede! Clean the Coffee machine!"
)

# save to file
response.stream_to_file(speech_file_path)
#
#
#
# store chats 
ch = sk.contacts["live:.cid.6cace4c66e5c4e19"].chat

# send voicemessage
with open("speech.mp3", "rb") as f:
    ch.sendFile(content = f, name = "reminder.mp3", image = False)

# # send message
# ch.sendMsg(message_response_text)
#
#
#
#
#
# while sk.chats.recent():
#     pass  # Just populate the cache.

# for chat in sk.chats:
#     print(chat.id)

ch = sk.chats["19:f001a4cf98cd4e0d877fc54006586918@thread.skype"]
ch.topic
ch.getMsgs()
#
#
#
#
