import requests

summary = requests.get(
    "http://127.0.0.1:8000/summarize",
    params={"url": "https://en.wikipedia.org/wiki/Special:Random"},
    timeout=10,
).json()["summary"]
print(summary)
