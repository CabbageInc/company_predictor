from transformers import pipeline

sentiment = pipeline(task='sentiment-analysis')
results = sentiment('i am good')

print(results)