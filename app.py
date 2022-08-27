import re

import requests
from bs4 import BeautifulSoup
from transformers import pipeline


def get_text_from_wikiepedia_article(url):
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    text = soup.find("div", {"id": "mw-content-text"}).text  # get body content text
    text = re.sub(r"\[\d+\]", "", text)  # remove all references
    text = text.split("\n\n")[0]  # keep only the first section of the wikipedia article
    text = text.strip()  # remove leading and trailing whitespaces
    return text


def main():
    summarizer = pipeline("summarization", model="t5-small")
    text = get_text_from_wikiepedia_article("https://en.wikipedia.org/wiki/Lorem_ipsum")
    print(text)
    summary = summarizer(text)[0]["summary_text"]
    print("-------------------------")
    print(summary)


if __name__ == "__main__":
    main()
