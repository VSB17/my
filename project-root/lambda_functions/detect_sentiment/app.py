import json
import boto3

comprehend_client = boto3.client('comprehend')

def lambda_handler(event, context):
    # Assuming the input event contains the text for sentiment analysis
    text = event.get('text', '')
    
    # Use AWS Comprehend to analyze sentiment
    response = comprehend_client.detect_sentiment(Text=text, LanguageCode='en')
    
    # Extract sentiment and confidence from the response
    sentiment = response['Sentiment']
    confidence = response['SentimentScore'][sentiment.capitalize()] * 100
    
    result = {
        'sentiment': sentiment,
        'confidence': confidence
    }
    
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }

