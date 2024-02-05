import json

def lambda_handler(event, context):
    # Process SQS event
    for record in event['Records']:
        # Assuming the message contains text for sentiment analysis
        message_body = json.loads(record['body'])
        text = message_body.get('text', '')
        
        # Your processing logic here, e.g., store in a database, trigger another service, etc.
        
        print(f"Received message for sentiment analysis: {text}")

    return {
        'statusCode': 200,
        'body': json.dumps('SQS message processing completed')
    }

