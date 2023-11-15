# type: ignore
# flake8: noqa
#
#
from skpy import Skype
from my_secrets import username, password

sk = Skype(username, password) # connect to Skype
#
#
#
#
# print(sk.user) # you
# print(sk.contacts["live:felix.mue"]) # your contacts
# print(sk.contacts["live:felix.mue"].chat.id)
# print(sk.chats.recent())

ch = sk.chats["8:live:felix.mue"]
ch.getMsgs()
#
#
#
#
#
#
