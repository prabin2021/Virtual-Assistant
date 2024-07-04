from transformers import pipeline

sentiment_analysis = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')
def analyze_sentiment(query):
        result = sentiment_analysis(query)[0]
        sentiment = result['label']
        confidence = result['score']
        return sentiment, confidence   