#!/usr/bin/env python3
from optparse import OptionParser
import requests
import socket
import json
import time
import sys
import re
import os

#parse options
parser = OptionParser()
parser.add_option("-w", "--webhook_url", dest="webhook_url", default="", help="sets webhook url")
parser.add_option("-u", "--user", dest="username", default=socket.gethostname(), help="sets username")
parser.add_option("-m", "--message", dest="content", default="default message", help="sets content of message")
parser.add_option("-a", "--avatar_url", dest="avatar_url", default="https://showme1-9071.kxcdn.com/pics/profile/avatar/fbavatar_53b75406810298d982889daa383874cf.jpg", help="sets avatar image to image on avatar_url")
parser.add_option("-t", "--tts", dest="tts", default="False", help="sets tts value (True/False)")
parser.add_option("-i", "--infile", dest="file", default="", help="sets file to attach") #not implemented
parser.add_option("-e", "--embed", dest="embeds", default="", help="sets page to embed") #not implemented
(options, args) = parser.parse_args()
url=options.webhook_url.strip()
username=options.username
content=options.content
avatar_url=options.avatar_url
tts=options.tts
filepath=options.file
embeds=options.embeds

#parsing etc
query = {}
paramnames = ["username", "content", "avatar_url", "tts", "filepath", "embeds"]
params = [username, content, avatar_url, tts, filepath, embeds]
for i in range(0,len(params)):
    if len(params[i]) > 0:
        query[paramnames[i]] = params[i]

#url checks
httpr = r"^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"
if len(url) == 0:
    print("Please provide webhook url with \"-w [url]\"")
    quit()
pattern = r"jpg$|png$"
if re.match(pattern, query[paramnames[2]]) and query[paramnames[2]] != "https://showme1-9071.kxcdn.com/pics/profile/avatar/fbavatar_53b75406810298d982889daa383874cf.jpg":
    print("Avatar URL OK")
if re.match(httpr, url):
    print("Webhook URL OK")

#posting
try:
    r = requests.get(url)
    data = json.loads(r.text)
    name = data["name"]
    channel_id = data["channel_id"]
    print("Sending to hook: "+name+" (Channel ID: "+channel_id+")")
except:
    print('Failed to open url.')
    if data["code"] is not None:
        print(data["code"])
if requests.post(url, data=query):
    print("Message sent (\""+content+"\")")
else:
    error = json.loads(requests.post(url, data=query).text)
    print("Message not sent. "+ error["message"])
    if error["message"] == 'You are being rate limited.':
        times = int(error["retry_after"] / 1000)
        for i in range(times, 0, -1):
            print(("Waiting %i seconds before retrying" % i), end='\r', file=sys.stdout, flush=True)
            time.sleep(1)
#TODO: modules/options & files
