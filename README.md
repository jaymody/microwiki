Summarizes wikipedia pages.

**Usage:**

Start API server:
```
 poetry run uvicorn app:app
```

Test the endpoint (local only):
```
poetry run python test.py
```

Download/save model weights in `model/`:
```
poetry run python download_model.py
```

Build docker image:
```
docker build -t microwiki .
```

Run docker image:
```
docker run -it -p 8000:8000 --rm microwiki
```
