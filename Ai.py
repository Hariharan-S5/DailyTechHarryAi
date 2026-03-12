# AI Deep Explanation
import json
from transformers import pipeline


# load metadata
with open("metadata.json") as f:
    meta = json.load(f)


MODEL_NAME = meta["ai_model"]["model_name"]
MAX_LEN = meta["bot_settings"]["ai_max_length"]
FILTER_LEN = meta["bot_settings"]["ai_filter_length"]
KEYWORDS = meta["keywords"]


# load AI model
generator = pipeline(
    "text-generation",
    model=MODEL_NAME
)


def explain(text):

    prompt = f"""
        Explain this software technology news clearly for a developer.

        News:
        {text}
    """

    result = generator(prompt, max_length=MAX_LEN)

    return result[0]["generated_text"]


def is_software_news(title, description):

    text = (title + " " + description).lower()

    # keyword filter (fast)
    for k in KEYWORDS:
        if k in text:
            return True

    # fallback AI classification
    prompt = f"""
        Is this news related to software technology,
        programming, AI tools, frameworks, cloud computing
        or developer tools?

        Answer only YES or NO.

        News:
        {text}
    """

    result = generator(prompt, max_length=FILTER_LEN)

    answer = result[0]["generated_text"].lower()

    return "yes" in answer
