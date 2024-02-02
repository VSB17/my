import json

def sqs_lambda_handler(event, context):
    for record in event['Records']:
        # Process the message from SQS
        body = json.loads(record['body'])
        print(f"Received message: {body}")
        # Perform Comprehend processing here
