from skpy import Skype
from my_secrets import username, password

# define username and password
sk = Skype(username, password)

# store chats 
ch = sk.chats["8:live:felix.mue"]

# send message
ch.sendMsg("cacacaccacrrrraaaaaab")
