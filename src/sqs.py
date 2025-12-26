import boto3

QUEUE_NAME = 'MyTest-SQS-Queue'
def sqs_client():
    sqs = boto3.client('sqs', region_name='ap-south-1')
    return sqs



def create_sqs_queue():
    return sqs_client().create_queue(
            QueueName=QUEUE_NAME
    )


if __name__ == '__main__':
    print(create_sqs_queue())
    