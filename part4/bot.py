import praw 
import time
import pyfiglet
import random 
import requests
import sys
from sys import exit




reddit = praw.Reddit(client_id="N_dXynqjpjdXgg",
                     client_secret="Fn8E9DEelnjXYQQcv1bbS2qLd48WiA",
                     password="PapayaOk1558",
                     user_agent="posted by u/PapayaOk1558",
                     username="PapayaOk1558")
 
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


title = input("Enter an epic title 1: ")
title2 = input("Enter an epic title 2: ") 
title3 = input("Enter an epic title 3: ")

url = input("Enter a sassy link 1: ")
url2 = input("Enter a sassy link 2: ")
url3 = input("Enter a sassy link 3: ")


comment = input ("Enter your comment 1: ")
comment2 = input ("Enter your comment 2: ") 
comment3 = input ("Enter your comment 3: ")

name = input ("Enter your comment 1: ")
name2 = input ("Enter your comment 2: ") 
name3 = input ("Enter your comment 3: ")

print("Reading reddit list")
subredit_list = open("data.txt", "r")
subreddits = subredit_list.read().split(',')

for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title,url=url)
    com = "###[meg@ pak]({}), {}".format(comment, name)
    time.sleep(10)
    submission.reply(com)
    print ("done")
  except Exception as err:
    print("Exception for subreddit {}, {}".format(subreddit, err))
  t= random.randint(600,700)
  seconds = "Sleeping for {} seconds before proceeding".format(t)
  print(seconds)
  time.sleep(t)

  print("Reading reddit list")
  subredit_list = open("data2.txt", "r")
  subreddits = subredit_list.read().split(',')

for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title2,url=url2)
    com = "###[pack mega]({}), {}".format(comment2, name2)
    time.sleep(10)
    submission.reply(com)
    print ("done")
  except Exception as err:
    print("Exception for subreddit {}, {}".format(subreddit, err))
  t= random.randint(650,700)
  seconds = "Sleeping for {} seconds before proceeding".format(t)
  print(seconds)
  time.sleep(t)

  print("Reading reddit list")
  subredit_list = open("data3.txt", "r")
  subreddits = subredit_list.read().split(',')

for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title3,url=url3)
    com = "###[mega pack]({}), {}".format(comment3, name3)
    time.sleep(10)
    submission.reply(com)
    print ("done")
  except Exception as err:
    print("Exception for subreddit {}, {}".format(subreddit, err))
  t= random.randint(600,720)
  seconds = "Sleeping for {} seconds before proceeding".format(t)
  print(seconds)
  time.sleep(t)
