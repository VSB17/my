import json
import boto3

def lambda_handler(event, context):
    try:
        # Extract S3 event details
        s3_records = event['Records']
        
        for record in s3_records:
            # Get the S3 bucket and object key
            bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']

            # Process the S3 event (e.g., perform some action on the uploaded object)
            # ...

        # Return a successful response
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'S3 event processed successfully'})
        }

    except Exception as e:
        # Handle any errors and return an error response
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }
