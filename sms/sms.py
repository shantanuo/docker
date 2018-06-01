import boto3
import os

client = boto3.client(
    "sns",
    aws_access_key_id=os.environ['DEV_ACCESS_KEY'],
    aws_secret_access_key=os.environ['DEV_SECRET_KEY'],
    region_name="us-east-1"
)

client.publish(
    PhoneNumber="+919819838466",
    Message="Hello World aws again from docker!",
   MessageAttributes={
    'AWS.SNS.SMS.SMSType': {
      'DataType': 'String',
      'StringValue': 'Transactional'
    }
  }
)
