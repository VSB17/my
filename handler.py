import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Received event: {}".format(json.dumps(event)))

    try:
        # Extract 'text' from the incoming request body
        request_body = json.loads(event['Records'][0]['body'])
        text = request_body.get('text')

        # Check if 'text' is present in the request
        if text is None:
            raise ValueError("Missing 'text' field in the request body")

        # Specify the language code (e.g., 'en' for English)
        language_code = 'en'

        # Call AWS Comprehend service to perform sentiment analysis
        comprehend = boto3.client('comprehend', region_name='ap-southeast-2')
        response = comprehend.detect_sentiment(Text=text, LanguageCode=language_code)

        # Log the response
        logger.info("Comprehend response: {}".format(json.dumps(response)))

        # Process the response as needed
        # Example: Extract sentiment result
        sentiment = response['Sentiment']
        logger.info("Sentiment: {}".format(sentiment))

        # TODO: Add your processing logic based on the Comprehend response
        # ...

        # Return a successful response
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }

    except Exception as e:
        # Log the error
        logger.error("Error processing request: {}".format(str(e)))

        # Handle any errors and return an error response
        return {
            'statusCode': 400,
            'body': json.dumps({
                '__type': 'ValidationException',
                'message': str(e)
            })
        }
