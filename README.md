# 🚀 DailyTechHarryAI – AI-Powered Software News Telegram Bot

## 📌 Project Description

**DailyTechAI** is an automated **AI-powered Telegram bot** that fetches the latest **software technology news**, filters relevant articles, and delivers them to users in a clean format.

The bot collects news from developer-focused RSS feeds, removes duplicates, and allows users to request **AI-generated explanations** for any news item directly inside Telegram.

It focuses on **software engineering topics** such as:

* Programming
* Java ecosystem
* AI tools
* Cloud computing
* DevOps
* Developer frameworks
* Software releases and updates

---

# 🎯 Project Purpose

The goal of this project is to build an **intelligent automation system** that:

       ✔ Fetches technology news automatically

       ✔ Filters only **software-related news**

       ✔ Sends updates to Telegram on a schedule

       ✔ Uses AI to explain complex news topics

       ✔ Prevents duplicate news delivery

This project demonstrates practical skills in:

* AI integration
* Automation systems
* API integrations
* Data processing
* Bot development
* Python backend design

---



## 🤖 Try the Bot

Click the link below to start using the Telegram bot:

[Open DailyTechHarryAI-Bot](https://web.telegram.org/k/#@DailyTechHarry_bot)

---

# 🏗 System Architecture

```
                                                     RSS Sources
                                                 (HackerNews, InfoQ)
                                                          │
                                                          ▼
                                                     News.py
                                                 (Fetch + Clean HTML)
                                                          │
                                                          ▼
                                                       Ai.py
                                              ┌────────────────────────┐
                                              │  Keyword Filtering     │
                                              │  AI Explanation Model  │
                                              └────────────────────────┘
                                                          │
                                                          ▼
                                                       main.py
                                               ┌──────────────────────┐
                                               │ Telegram Bot Logic   │
                                               │ Scheduler            │
                                               │ Duplicate Detection  │
                                               └──────────────────────┘
                                                          │
                                                          ▼
                                                      Telegram Bot
                                                          │
                                                          ▼
                                                      User Interaction
```




# ⚙️ Installation Guide

Follow the steps below to run **DailyTechAI Telegram Bot** locally.

---

# 🌱 Environment Variables (.env)

To securely store API keys and secrets, use a `.env` file in your project root. Example:

```
TELEGRAM_NEWS_API_KEY=your_api_key_here
```

Install the `python-dotenv` package to load environment variables automatically:

```bash
pip install python-dotenv
```

Add this code snippet at the top of your main Python files (e.g., `News.py`):

```python
from dotenv import load_dotenv
load_dotenv()
```

This will load variables from `.env` so you don’t need to set them manually each time.

---

# 1️⃣ Clone the Repository

```bash
git clone https://github.com/Hariharan-S5/DailyTechHarryAI.git
cd DailyTechAI
```

---

# 2️⃣ Install Python Dependencies

Install the required libraries using `pip`.

### Core Libraries

```bash
pip install requests transformers torch schedule
```

### RSS Feed Parser

```bash
pip install feedparser
```

### HTML Cleaning Library

```bash
pip install beautifulsoup4
```

---

# 3️⃣ (Optional) Install All Dependencies at Once

You can also install everything in one command:

```bash
pip install requests transformers torch schedule feedparser beautifulsoup4
```

---

# 4️⃣ Configure Bot Settings

Edit the configuration file:

```bash
.env
```

Add your Telegram bot credentials:

```.env
TELEGRAM_BOT_TOKEN=0000000:XAXAXAXAXAXAXAXAXAXAXAXAXAXA
TELEGRAM_CHAT_ID=0000000000
TELEGRAM_NEWS_API_KEY=XA0XA0XA0XA0XA0XA0XA0
```

---

# 5️⃣ Run the Bot

Start the bot using:

```bash
python main.py
```

The bot will now:

* Fetch software development news
* Filter relevant topics
* Send updates to Telegram
* Provide AI explanations on request

---

# 🐍 Python Version

Recommended Python version:

```bash
Python 3.9+
```

---

# 📦 Dependency Summary

| Library        | Purpose               |
| -------------- | --------------------- |
| requests       | API communication     |
| transformers   | AI model inference    |
| torch          | Deep learning backend |
| schedule       | Task scheduling       |
| feedparser     | RSS news parsing      |
| beautifulsoup4 | HTML cleaning         |



# ⚙️ Project Workflow

### Step 1 — Fetch News

`News.py` retrieves RSS feeds from technology sources.

Example feeds:

* Hacker News
* InfoQ Java Feed

The module also removes HTML tags from the description.

---

### Step 2 — Filter Software News

`Ai.py` filters only relevant news using:

1️⃣ Keyword filtering
2️⃣ AI-based explanation generation

Example keywords:

```
software
programming
java
spring
ai
cloud
docker
kubernetes
devops
database
github
```

---

### Step 3 — Remove Duplicate News

`main.py` stores sent news titles inside:

```
sent_news.json
```

Before sending news, the system checks:

```
if title in sent_news:
    skip
```

This ensures users **never receive the same news twice**.

---

### Step 4 — Send News to Telegram

The bot sends formatted messages:

```
🚀 Daily Software Tech Updates

1. 📰 Title
2. 📄 Description
3. 🔗 Link

💬 Reply with number for AI explanation
```

---

### Step 5 — AI Explanation

When a user replies with a number:

```
1
```

The bot sends an AI explanation for that news article.

---

# 🤖 AI Model Information

The project uses the Hugging Face model:

**Model:** `google/flan-t5-base`

Purpose:

* Natural language explanation
* Summarizing technical news
* Generating developer-friendly explanations

Example prompt:

```
Explain this software technology news clearly:
```

The model then generates a simplified explanation.

---

# 🧠 AI Filtering Logic

The system uses a **hybrid filtering approach**.

### Layer 1 – Keyword Detection

Fast filtering using metadata keywords.

### Layer 2 – AI Explanation

Used when a user asks for deeper understanding.

---

# 🌐 News Sources

The system collects data from RSS feeds.

| Source          | Purpose                |
| --------------- | ---------------------- |
| Hacker News     | General developer news |
| InfoQ Java Feed | Java ecosystem updates |

Example RSS feeds used:

```
https://hnrss.org/frontpage
https://www.infoq.com/java/feed/
```

---

# 🗂 Project Structure

```
DailyTechAI
│
├── main.py
├── Ai.py
├── News.py
├── metadata.json
├── sent_news.json
├── .env
└── README.md

```

---

# 📦 Module Explanation

## 1️⃣ main.py

Main Telegram bot controller.

Responsibilities:

* Schedule news delivery
* Process Telegram messages
* Prevent duplicate news
* Send AI explanations

---

## 2️⃣ Ai.py

AI module responsible for:

* News explanation
* Keyword filtering
* AI prompt generation

---

## 3️⃣ News.py

Handles:

* Fetching RSS feeds
* Parsing XML
* Cleaning HTML tags
* Formatting news data

---

## 4️⃣ metadata.json

Configuration file controlling:

Prodection 
```
    true : live/production mode, 
    false : testing/development mode
```

Schedule settings
```
    Set the timing for news delivery (e.g., interval, cron)
```

RSS sources
```
    List of RSS feed URLs for news collection
```

News limits
```
    Maximum number of news items to fetch/send per cycle
```

AI model
```
    Model name or path used for AI explanations
```

Keywords
```
    List of keywords for filtering relevant news
```


This allows easy system customization without editing code.

---

# ⏰ Scheduling System

The bot can run in:

### Development Mode

```
Every X seconds
```

### Production Mode

```
Every X hours
```

Configured inside:

```
metadata.json
```

---

# 📡 Telegram Integration

The bot communicates with Telegram using the **Telegram Bot API**.

Key API endpoints used:

```
sendMessage
getUpdates
```

Features supported:

* Automatic news delivery
* Interactive AI explanations
* User command responses

---

# 🔒 Duplicate News Prevention

Sent news titles are stored locally:

```
sent_news.json
```

Before sending a news article:

```
check if title already exists
```

If yes → skip.

---

# 🧩 Technologies Used

| Technology    | Purpose            |
| ------------- | ------------------ |
| Python        | Core development   |
| Transformers  | AI model inference |
| Feedparser    | RSS parsing        |
| BeautifulSoup | HTML cleaning      |
| Schedule      | Task automation    |
| Requests      | API communication  |

---

# 🚀 Example Bot Output

```
🚀 Daily Software Tech Updates

📰 Title: Java Virtual Threads Improve Performance

📄 Description:
Java introduces lightweight threads enabling massive concurrency improvements.

🔗 https://example.com

💬 Reply with number for AI explanation
```

User response:

```
1
```

Bot reply:

```
Virtual threads allow Java applications to handle thousands of tasks simultaneously with minimal memory usage...
```

---

# 📈 Future Improvements

Planned enhancements:

* GitHub trending repository updates
* AI-generated news summaries
* News categorization (AI, Cloud, DevOps)
* Database storage for news history
* Web dashboard for analytics

---

# 🧾 Conclusion

**DailyTechAI** demonstrates how AI, automation, and APIs can be combined to create an intelligent information system for developers.

The project highlights:

* AI integration in real applications
* Real-time data processing
* Automation workflows
* Telegram bot development

This system can evolve into a **full developer news assistant platform**.

---


