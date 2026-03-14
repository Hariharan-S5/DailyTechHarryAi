# News fetching module for DailyTechAi
import json
import feedparser
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

# load metadata
with open("metadata.json") as f:
    meta = json.load(f)

load_dotenv()

HACKERNEWS_URL = meta["rss_sources"]["hackernews"]
INFOQ_URL = meta["rss_sources"]["infoq_java"]

HN_LIMIT = meta["news_limit"]["hackernews"]
JAVA_LIMIT = meta["news_limit"]["infoq_java"]

print(os.getenv("TELEGRAM_BOT_TOKEN"))
print(os.getenv("TELEGRAM_NEWS_API_KEY"))
API_KEY = os.getenv("TELEGRAM_NEWS_API_KEY")


def clean_html(text):

    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


def get_news():

    tech = feedparser.parse(HACKERNEWS_URL)
    java = feedparser.parse(INFOQ_URL)

    news_list = []

    # HackerNews
    for entry in tech.entries[:HN_LIMIT]:

        desc = clean_html(entry.summary)

        news_list.append({
            "title": entry.title,
            "description": desc,
            "link": entry.link
        })

    # InfoQ Java
    for entry in java.entries[:JAVA_LIMIT]:

        desc = clean_html(entry.summary)

        news_list.append({
            "title": entry.title,
            "description": desc,
            "link": entry.link
        })

    return news_list

