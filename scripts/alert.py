import json
import boto3

def lambda_handler(event, context):
    TOPIC_ARN = '' # The ARN of the SNS topic
    sns = boto3.client('sns')
    subject = 'Comixology: New releases'
    message = 'The Comixology new releases have been successfully uploaded to S3'
    result = sns.publish(TopicArn=TOPIC_ARN, Message=message, Subject=subject)