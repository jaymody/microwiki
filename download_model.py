from transformers import pipeline

summarizer = pipeline(
    "summarization", model="t5-small", clean_up_tokenization_spaces=True
)
summarizer.save_pretrained("model/")
