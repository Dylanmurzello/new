import praw 
import time
import pyfiglet
import random 
import requests
import sys
from sys import exit




reddit = praw.Reddit(client_id="1Ty0TbyDBIt0lw",
                     client_secret="GpKnQostc_PpSMzbdr9cUEqU7-X8cw",
                     password="Objective-Cat-4310",
                     user_agent="posted by u/Objective-Cat-4310",
                     username="Objective-Cat-4310")
 
result = pyfiglet.figlet_format("Dylan OP") 
print(result) 

print("Starting Magic............")

print(reddit.user.me())

REDDIT_USERNAME=(reddit.user.me())

response = requests.get("https://www.reddit.com/user/{}/about.json".format(REDDIT_USERNAME),  headers = {'User-agent': 'hiiii its {}'.format(REDDIT_USERNAME)}).json()
if "error" in response:
 if response["error"] == 404:
      print("account {} is shadowbanned. poor bot :( shutting down the script...".format(REDDIT_USERNAME))
      sys.exit()
 else:
      print(response)
else:
    print("{} is not shadowbanned! We think..".format(REDDIT_USERNAME))




data = {}
count = 0
subredit_list = []
title_list = []
url_list = []
comment_list = []
name_list = []

print("Reading reddit list")
subredit = open("data.txt", "r")
for line in subredit:
    subredit_list.append(line.strip())

print("Reading title list")
title = open("title.txt", "r",  encoding="utf8")
for line in title:
    title_list.append(line.strip())

print("Reading url list")
url = open("url.txt", "r")
for line in url:
    url_list.append(line.strip())

print("Reading comment list")
comment = open("comment.txt", "r", encoding="utf8")
for line in comment:
    comment_list.append(line.strip())
    
print("Reading name list")
comment = open("name.txt", "r", encoding="utf8")
for line in comment:
    comment_list.append(line.strip())
    
for i in range(0, len(title_list)):
    for k in range(0, len(subredit_list)):
        try:
            # added code from above
            REDDIT_USERNAME = (reddit.user.me())

            response = requests.get("https://www.reddit.com/user/{}/about.json".format(REDDIT_USERNAME),
                                    headers={'User-agent': 'hiiii its {}'.format(REDDIT_USERNAME)}).json()
            if "error" in response:
                if response["error"] == 404:
                    print("account {} is shadowbanned. poor bot :( shutting down the script...".format(REDDIT_USERNAME))
                    sys.exit()
                else:
                    print(response)
            else:
                print("{} is not shadowbanned! We think..".format(REDDIT_USERNAME))

            print(subredit_list[k])
            print(title_list[i])
            print(url_list[i])
            print(comment_list[i])
            reddit.validate_on_submit = True
            submission = reddit.subreddit(subredit_list[k]).submit(title_list[i], url=url_list[i])
            com = "#[Album pack]({}),({}) ".format(comment_list[i], name_list[i])
            time.sleep(10)
            submission.reply(com)
            print("done")
        except Exception as err:
            print("Exception for subreddit {}, {}".format(subredit_list[k], err))
        t = random.randint(650, 700)
        seconds = "Sleeping for {} seconds before proceeding".format(t)
        print(seconds)
        time.sleep(t)
