import requests
import socket
import re
import json
#
#          LEMONADE'S
#     VSV DISCORD POST BOT
#    POST MESSAGES TO "BOT"
#        CHANNEL (VSV)
#
#   CHANGE PARAMS TO LIKING
#       HAVE FUN NERDS
#

#Webhook URL
#-- best afblijven (tenzij ge dit gebruikt voor een andere server)
url = "https://discordapp.com/api/webhooks/454652577251065866/jMGBA1bDAeN0bzhFSqidyCQRlFithWYjfayWyAhCodeG0PHORSpVdL2go9p6lSDfA5Ad"

#PARAMS
#USERNAME
#-- default hostname
username = "PaTee's Woke Woker"

#MESSAGE CONTENT
#-- default filler
content = "<@!326444539537522688>"

#SET AVATAR URL
#-- default swennen met koffie
avatar_url = "https://newgateclocks.com/media/catalog/product/cache/10/image/9df78eab33525d08d6e5fb8d27136e95/n/u/numone149fer_-_number_one_echo_-_fire_engine_red_1.png"

#TTS = Text To Speech
#-- default false
tts="true"

#FILE TO OPEN (ENTER PATH)
#-- optional default empty (TODO -- werkt niet)
filepath=""
    
#EMBED LINKS (yt videos enzo denk ik)
#-- optional default emptt
embeds=""


#AFBLIJVEN -- BELANGRIJKE SHIT
query = {}
paramnames = ["username", "content", "avatar_url", "tts", "filepath", "embeds"]
params = [username, content, avatar_url, tts, filepath, embeds]
for i in range(0,len(params)):
    if len(params[i]) > 0:
        query[paramnames[i]] = params[i]
#defaults
httpr = r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"
if len(params[0]) == 0:
    query[paramnames[0]] = socket.gethostname()
if len(params[1]) == 0:
    query[paramnames[1]] = socket.gethostname()+" is vergeten content in te vullen, haha"
if len(params[2]) == 0 or not re.match(httpr, avatar_url):
    query[paramnames[2]] = "https://showme1-9071.kxcdn.com/pics/profile/avatar/fbavatar_53b75406810298d982889daa383874cf.jpg"
if len(params[3]) == 0 or (params[3] != "true" or params[3] != "false"):
    query[paramnames[3]] = "false"
#avatar_url check
pattern = r"jpg$|png$"
if re.match(pattern, query[paramnames[2]]) and query[paramnames[2]] != "https://showme1-9071.kxcdn.com/pics/profile/avatar/fbavatar_53b75406810298d982889daa383874cf.jpg":
    print("Avatar URL OK")
if re.match(httpr, url):
    print("Webhook URL OK")
try:
    r = requests.get(url)
    data = json.loads(r.text)
    name = data["name"]
    channel_id = data["channel_id"]
    print("Sending to hook: "+name+" (Channel ID: "+channel_id+")")
except ConnectionError:
    print('Failed to open url.')
if requests.post(url, data=query):
    print("Message sent")
else:
    print("Message failed to send. "+json.loads(requests.post(url, data=query).text)["message"])
#TODO: modules en files