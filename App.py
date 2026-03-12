#  Telegram Bot Logic
import requests
import schedule
import time
import json
import os

from News import get_news
from Ai import explain, is_software_news


# LOAD METADATA CONFIG
with open("metadata.json") as f:
    config = json.load(f)

PRODUCTION = config["production"]
TOKEN = config["telegram"]["bot_token"]
CHAT_ID = config["telegram"]["chat_id"]

SENT_FILE = config["files"]["sent_news_file"]


ROCKET = "\U0001F680"
NEWS = "\U0001F4F0"
DOC = "\U0001F4C4"
LINK = "\U0001F517"
CHAT = "\U0001F4AC"

SCHEDULE_HOURS = config["bot_settings"]["schedule_hours"]
SCHEDULE_MINUTES = config["bot_settings"]["schedule_minutes"]
SCHEDULE_SECOND = config["bot_settings"]["schedule_seconds"]


news_cache = []
last_update_id = None


# LOAD SENT NEWS
if os.path.exists(SENT_FILE):
    with open(SENT_FILE, "r") as f:
        sent_news = set(json.load(f))
else:
    sent_news = set()


def save_sent_news():
    with open(SENT_FILE, "w") as f:
        json.dump(list(sent_news), f)


def send_news():

    global news_cache

    news = get_news()

    filtered_news = []

    for n in news:

        title = n["title"]
        description = n.get("description", "")

        # skip duplicate
        if title in sent_news:
            continue

        # AI filter
        if is_software_news(title, description):

            filtered_news.append(n)
            sent_news.add(title)

    if not filtered_news:
        print("No new relevant news")
        return

    news_cache = filtered_news

    save_sent_news()

    message = f"{ROCKET} Daily Software Tech Updates\n\n"

    for i, n in enumerate(news_cache):

        message += (
            f"{i+1}. {NEWS} *Title:* {n['title']}\n"
            f"{DOC} *Description:* {n.get('description','')[:150]}...\n"
            f"{LINK} {n['link']}\n\n"
        )

    message += f"{CHAT} Reply with number for AI explanation."

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    res = requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    })



def check_messages():

    global last_update_id

    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

    if last_update_id:
        url += f"?offset={last_update_id + 1}"

    res = requests.get(url).json()

    if not res["result"]:
        return

    for update in res["result"]:

        last_update_id = update["update_id"]

        if "message" not in update:
            continue

        msg = update["message"]["text"]

        if msg.isdigit():

            index = int(msg) - 1

            if index < len(news_cache):

                news = news_cache[index].get("description") or news_cache[index]["title"]

                answer = explain(news)

                send_message(answer)


def send_message(text):

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    })


# SCHEDULE FROM METADATA
if(PRODUCTION): 
    schedule.every(SCHEDULE_HOURS).hours.do(send_news)
else:
    schedule.every(SCHEDULE_SECOND).seconds.do(send_news)


while True:

    schedule.run_pending()

    check_messages()

    time.sleep(10)

