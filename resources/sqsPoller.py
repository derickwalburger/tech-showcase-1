import boto3
import sys

# Get the service resource
sqs = boto3.client('sqs', region_name='us-west-2', aws_access_key_id='AKIAIGPK4KUBF4HIY7KQ', aws_secret_access_key='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')
queueName = sys.argv[1]

print(queueName)

url = sqs.get_queue_url(QueueName=queueName)["QueueUrl"]

while True:
    messages = sqs.receive_message(QueueUrl=url, MaxNumberOfMessages=1, WaitTimeSeconds=10)
    if 'Messages' in messages:
        for message in messages['Messages']:
            sqs.delete_message(QueueUrl=url,ReceiptHandle=message['ReceiptHandle'])

            print(message['Body'])
            if(message['Body'] == "True"):
                sys.exit(0)
            else:
                sys.exit(1)
    else:
        print('Timeout - try again')
