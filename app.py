import re

import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from transformers import pipeline

app = FastAPI(title="Wikipedia page summarizer.")


def get_text_from_wikipedia_article(url):
    html = requests.get(url, timeout=10).text
    soup = BeautifulSoup(html, "html.parser")
    text = soup.find("div", {"id": "mw-content-text"}).text  # get body content text
    text = re.sub(r"\[\d+\]", "", text)  # remove all references
    text = text.split("\n\n")[0]  # keep only the first section of the wikipedia article
    text = text.strip()  # remove leading and trailing whitespaces
    return text


def summarize(text):
    summarizer = pipeline(
        "summarization", model="model/", clean_up_tokenization_spaces=True
    )
    summary = summarizer(text)[0]["summary_text"]
    return summary


@app.get("/summarize")
def summarize_wikipedia_page(url: str):
    text = get_text_from_wikipedia_article(url)
    summary = summarize(text)
    print(text)
    print("-------------------------")
    print(summary)
    return {"summary": summary}
