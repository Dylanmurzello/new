import praw 
import time
import pyfiglet
import random 
import requests
import sys
from sys import exit




reddit = praw.Reddit(client_id="St-JdiL2jU1WJQ",
                     client_secret="BkArjRywIHzbIvnQfeo-sOS4sZlp8Q",
                     password="Wide_Tank4525",
                     user_agent="posted by u/Wide_Tank4525",
                     username="Wide_Tank4525")
 
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
title4 = input("Enter an epic title 4: ")
title5 = input("Enter an epic title 5: ")
title6 = input("Enter an epic title 6: ")
title7 = input("Enter an epic title 7: ") 
title8 = input("Enter an epic title 8: ")
title9 = input("Enter an epic title 9: ")
title10 = input("Enter an epic title 10: ")
title11 = input("Enter an epic title 11: ")
title12 = input("Enter an epic title 12: ") 
title13 = input("Enter an epic title 13: ")
title14 = input("Enter an epic title 14: ")
title15 = input("Enter an epic title 15: ")
title16 = input("Enter an epic title 16: ")
title17 = input("Enter an epic title 17: ") 
title18 = input("Enter an epic title 18: ")
title19 = input("Enter an epic title 19: ")
title20 = input("Enter an epic title 20: ")
title21 = input("Enter an epic title 21: ")
title22 = input("Enter an epic title 22: ") 
title23 = input("Enter an epic title 23: ")
title24 = input("Enter an epic title 24: ")
title25 = input("Enter an epic title 25: ")
title26 = input("Enter an epic title 26: ")

url = input("Enter an epic url 1: ")
url2 = input("Enter an epic url 2: ") 
url3 = input("Enter an epic url 3: ")
url4 = input("Enter an epic url 4: ")
url5 = input("Enter an epic url 5: ")
url6 = input("Enter an epic url 6: ")
url7 = input("Enter an epic url 7: ") 
url8 = input("Enter an epic url 8: ")
url9 = input("Enter an epic url 9: ")
url10 = input("Enter an epic url 10: ")
url11 = input("Enter an epic url 11: ")
url12 = input("Enter an epic url 12: ") 
url13 = input("Enter an epic url 13: ")
url14 = input("Enter an epic url 14: ")
url15 = input("Enter an epic url 15: ")
url16 = input("Enter an epic url 16: ")
url17 = input("Enter an epic url 17: ") 
url18 = input("Enter an epic url 18: ")
url19 = input("Enter an epic url 19: ")
url20 = input("Enter an epic url 20: ")
url21 = input("Enter an epic url 21: ")
url22 = input("Enter an epic url 22: ") 
url23 = input("Enter an epic url 23: ")
url24 = input("Enter an epic url 24: ")
url25 = input("Enter an epic url 25: ")
url26 = input("Enter an epic url 26: ")

comment = input("Enter an epic comment 1: ")
comment2 = input("Enter an epic comment 2: ") 
comment3 = input("Enter an epic comment 3: ")
comment4 = input("Enter an epic comment 4: ")
comment5 = input("Enter an epic comment 5: ")
comment6 = input("Enter an epic comment 6: ")
comment7 = input("Enter an epic comment 7: ") 
comment8 = input("Enter an epic comment 8: ")
comment9 = input("Enter an epic comment 9: ")
comment10 = input("Enter an epic comment 10: ")
comment11 = input("Enter an epic comment 11: ")
comment12 = input("Enter an epic comment 12: ") 
comment13 = input("Enter an epic comment 13: ")
comment14 = input("Enter an epic comment 14: ")
comment15 = input("Enter an epic comment 15: ")
comment16 = input("Enter an epic comment 16: ")
comment17 = input("Enter an epic comment 17: ") 
comment18 = input("Enter an epic comment 18: ")
comment19 = input("Enter an epic comment 19: ")
comment20 = input("Enter an epic comment 20: ")
comment21 = input("Enter an epic comment 21: ")
comment22 = input("Enter an epic comment 22: ") 
comment23 = input("Enter an epic comment 23: ")
comment24 = input("Enter an epic comment 24: ")
comment25 = input("Enter an epic comment 25: ")
comment26 = input("Enter an epic comment 26: ")

name = input("Enter an epic name 1: ")
name2 = input("Enter an epic name 2: ") 
name3 = input("Enter an epic name 3: ")
name4 = input("Enter an epic name 4: ")
name5 = input("Enter an epic name 5: ")
name6 = input("Enter an epic name 6: ")
name7 = input("Enter an epic name 7: ") 
name8 = input("Enter an epic name 8: ")
name9 = input("Enter an epic name 9: ")
name10 = input("Enter an epic name 10: ")
name11 = input("Enter an epic name 11: ")
name12 = input("Enter an epic name 12: ") 
name13 = input("Enter an epic name 13: ")
name14 = input("Enter an epic name 14: ")
name15 = input("Enter an epic name 15: ")
name16 = input("Enter an epic name 16: ")
name17 = input("Enter an epic name 17: ") 
name18 = input("Enter an epic name 18: ")
name19 = input("Enter an epic name 19: ")
name20 = input("Enter an epic name 20: ")
name21 = input("Enter an epic name 21: ")
name22 = input("Enter an epic name 22: ") 
name23 = input("Enter an epic name 23: ")
name24 = input("Enter an epic name 24: ")
name25 = input("Enter an epic name 25: ")
name26 = input("Enter an epic name 26: ")

print("Reading reddit list")
subredit_list = open("data.txt", "r")
subreddits = subredit_list.read().split(',')

for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title,url=url)
    com = "###[meg@ pak album]({}), {}".format(comment, name)
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
    com = "###[hot pack mega]({}), {}".format(comment2, name2)
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
  
  print("Reading reddit list")
  subredit_list = open("data4.txt", "r")
  subreddits = subredit_list.read().split(',')
  
for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title4,url=url4)
    com = "###[mega pack]({}), {}".format(comment4, name4)
    time.sleep(10)
    submission.reply(com)
    print ("done")
  except Exception as err:
    print("Exception for subreddit {}, {}".format(subreddit, err))
  t= random.randint(600,710)
  seconds = "Sleeping for {} seconds before proceeding".format(t)
  print(seconds)
  time.sleep(t)
  
  print("Reading reddit list")
  subredit_list = open("data5.txt", "r")
  subreddits = subredit_list.read().split(',')
  
for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title5,url=url5)
    com = "###[mega pack]({}), {}".format(comment5, name5)
    time.sleep(10)
    submission.reply(com)
    print ("done")
  except Exception as err:
    print("Exception for subreddit {}, {}".format(subreddit, err))
  t= random.randint(600,750)
  seconds = "Sleeping for {} seconds before proceeding".format(t)
  print(seconds)
  time.sleep(t)
  
print("Reading reddit list")
subredit_list = open("data.txt", "r")
subreddits = subredit_list.read().split(',')

for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title6,url=url6)
    com = "###[meg@ pak]({}), {}".format(comment6, name6)
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
    submission = reddit.subreddit(subreddit).submit(title7,url=url7)
    com = "###[pack mega]({}), {}".format(comment7, name7)
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
    submission = reddit.subreddit(subreddit).submit(title8,url=url8)
    com = "###[mega pack]({}), {}".format(comment8, name8)
    time.sleep(10)
    submission.reply(com)
    print ("done")
  except Exception as err:
    print("Exception for subreddit {}, {}".format(subreddit, err))
  t= random.randint(600,720)
  seconds = "Sleeping for {} seconds before proceeding".format(t)
  print(seconds)
  time.sleep(t)
  
  print("Reading reddit list")
  subredit_list = open("data4.txt", "r")
  subreddits = subredit_list.read().split(',')
  
for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title9,url=url9)
    com = "###[mega pack]({}), {}".format(comment9, name9)
    time.sleep(10)
    submission.reply(com)
    print ("done")
  except Exception as err:
    print("Exception for subreddit {}, {}".format(subreddit, err))
  t= random.randint(600,710)
  seconds = "Sleeping for {} seconds before proceeding".format(t)
  print(seconds)
  time.sleep(t)
  
  print("Reading reddit list")
  subredit_list = open("data5.txt", "r")
  subreddits = subredit_list.read().split(',')
  
for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title10,url=url10)
    com = "###[mega pack]({}), {}".format(comment10, name10)
    time.sleep(10)
    submission.reply(com)
    print ("done")
  except Exception as err:
    print("Exception for subreddit {}, {}".format(subreddit, err))
  t= random.randint(600,750)
  seconds = "Sleeping for {} seconds before proceeding".format(t)
  print(seconds)
  time.sleep(t)
  
print("Reading reddit list")
subredit_list = open("data.txt", "r")
subreddits = subredit_list.read().split(',')

for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title11,url=url11)
    com = "###[meg@ pak]({}), {}".format(comment11, name11)
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
    submission = reddit.subreddit(subreddit).submit(title12,url=url12)
    com = "###[pack mega]({}), {}".format(comment12, name12)
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
    submission = reddit.subreddit(subreddit).submit(title13,url=url13)
    com = "###[mega pack]({}), {}".format(comment13, name13)
    time.sleep(10)
    submission.reply(com)
    print ("done")
  except Exception as err:
    print("Exception for subreddit {}, {}".format(subreddit, err))
  t= random.randint(600,720)
  seconds = "Sleeping for {} seconds before proceeding".format(t)
  print(seconds)
  time.sleep(t)
  
  print("Reading reddit list")
  subredit_list = open("data4.txt", "r")
  subreddits = subredit_list.read().split(',')
  
for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title14,url=url14)
    com = "###[mega pack]({}), {}".format(comment14, name14)
    time.sleep(10)
    submission.reply(com)
    print ("done")
  except Exception as err:
    print("Exception for subreddit {}, {}".format(subreddit, err))
  t= random.randint(600,710)
  seconds = "Sleeping for {} seconds before proceeding".format(t)
  print(seconds)
  time.sleep(t)
  
  print("Reading reddit list")
  subredit_list = open("data5.txt", "r")
  subreddits = subredit_list.read().split(',')
  
for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title15,url=url15)
    com = "###[mega pack]({}), {}".format(comment15, name15)
    time.sleep(10)
    submission.reply(com)
    print ("done")
  except Exception as err:
    print("Exception for subreddit {}, {}".format(subreddit, err))
  t= random.randint(600,750)
  seconds = "Sleeping for {} seconds before proceeding".format(t)
  print(seconds)
  time.sleep(t)
  
print("Reading reddit list")
subredit_list = open("data.txt", "r")
subreddits = subredit_list.read().split(',')

for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title16,url=url16)
    com = "###[meg@ pak]({}), {}".format(comment16, name16)
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
    submission = reddit.subreddit(subreddit).submit(title17,url=url17)
    com = "###[pack mega]({}), {}".format(comment17, name17)
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
    submission = reddit.subreddit(subreddit).submit(title18,url=url18)
    com = "###[mega pack]({}), {}".format(comment18, name18)
    time.sleep(10)
    submission.reply(com)
    print ("done")
  except Exception as err:
    print("Exception for subreddit {}, {}".format(subreddit, err))
  t= random.randint(600,720)
  seconds = "Sleeping for {} seconds before proceeding".format(t)
  print(seconds)
  time.sleep(t)
  
  print("Reading reddit list")
  subredit_list = open("data4.txt", "r")
  subreddits = subredit_list.read().split(',')
  
for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title19,url=url19)
    com = "###[mega pack]({}), {}".format(comment19, name19)
    time.sleep(10)
    submission.reply(com)
    print ("done")
  except Exception as err:
    print("Exception for subreddit {}, {}".format(subreddit, err))
  t= random.randint(600,710)
  seconds = "Sleeping for {} seconds before proceeding".format(t)
  print(seconds)
  time.sleep(t)
  
  print("Reading reddit list")
  subredit_list = open("data5.txt", "r")
  subreddits = subredit_list.read().split(',')
  
for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title20,url=url20)
    com = "###[mega pack]({}), {}".format(comment20, name20)
    time.sleep(10)
    submission.reply(com)
    print ("done")
  except Exception as err:
    print("Exception for subreddit {}, {}".format(subreddit, err))
  t= random.randint(600,750)
  seconds = "Sleeping for {} seconds before proceeding".format(t)
  print(seconds)
  time.sleep(t)
  
print("Reading reddit list")
subredit_list = open("data.txt", "r")
subreddits = subredit_list.read().split(',')

for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title21,url=url21)
    com = "###[meg@ pak]({}), {}".format(comment21, name21)
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
    submission = reddit.subreddit(subreddit).submit(title22,url=url22)
    com = "###[pack mega]({}), {}".format(comment22, name22)
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
    submission = reddit.subreddit(subreddit).submit(title23,url=url23)
    com = "###[mega pack]({}), {}".format(comment23, name23)
    time.sleep(10)
    submission.reply(com)
    print ("done")
  except Exception as err:
    print("Exception for subreddit {}, {}".format(subreddit, err))
  t= random.randint(600,720)
  seconds = "Sleeping for {} seconds before proceeding".format(t)
  print(seconds)
  time.sleep(t)
  
  print("Reading reddit list")
  subredit_list = open("data4.txt", "r")
  subreddits = subredit_list.read().split(',')
  
for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title24,url=url24)
    com = "###[mega pack]({}), {}".format(comment24, name24)
    time.sleep(10)
    submission.reply(com)
    print ("done")
  except Exception as err:
    print("Exception for subreddit {}, {}".format(subreddit, err))
  t= random.randint(600,710)
  seconds = "Sleeping for {} seconds before proceeding".format(t)
  print(seconds)
  time.sleep(t)
  
  print("Reading reddit list")
  subredit_list = open("data5.txt", "r")
  subreddits = subredit_list.read().split(',')
  
for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title25,url=url25)
    com = "###[mega pack]({}), {}".format(comment25, name25)
    time.sleep(10)
    submission.reply(com)
    print ("done")
  except Exception as err:
    print("Exception for subreddit {}, {}".format(subreddit, err))
  t= random.randint(600,750)
  seconds = "Sleeping for {} seconds before proceeding".format(t)
  print(seconds)
  time.sleep(t)
  
for subreddit in subreddits:
  try:
    print(subreddit)
    reddit.validate_on_submit = True
    submission = reddit.subreddit(subreddit).submit(title26,url=url26)
    com = "###[mega pack]({}), {}".format(comment26, name26)
    time.sleep(10)
    submission.reply(com)
    print ("done")
  except Exception as err:
    print("Exception for subreddit {}, {}".format(subreddit, err))
  t= random.randint(600,750)
  seconds = "Sleeping for {} seconds before proceeding".format(t)
  print(seconds)
  time.sleep(t)
