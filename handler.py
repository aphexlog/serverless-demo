import json
from os import environ

def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    dynamoArn = environ.get("DYNAMODB_TABLE_NAME")
    s3Arn = environ.get("S3_BUCKET_ARN")

    print(dynamoArn)
    print(s3Arn)

    return {"statusCode": 200, "body": json.dumps(body)}
