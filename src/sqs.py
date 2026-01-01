import boto3

QUEUE_NAME = 'MyTest-SQS-Queue'
QUEUE_NAME_URL = "https://sqs.ap-south-1.amazonaws.com/743472496366/MyTest-SQS-Queue"
FIFO_QUEUE_NAME = 'MyTestQueue.fifo'


def sqs_client():
    sqs = boto3.client('sqs', region_name='ap-south-1')
    return sqs



def create_sqs_queue():
    return sqs_client().create_queue(
            QueueName=QUEUE_NAME
    )


def create_fifo_queue():
    return sqs_client().create_queue(
        QueueName=FIFO_QUEUE_NAME,
        Attributes={
            "FifoQueue": 'true'
        }
    )

if __name__ == '__main__':
    #print(create_sqs_queue())
    print(create_fifo_queue())