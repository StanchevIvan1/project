import logging

import boto3


class SESservice:
    def __init__(self):
        self.client = boto3.client('ses',
                                   aws_access_key_id='',
                                   aws_secret_access_key='',
                                   region_name="eu-central-1")

    def send_email(self, email):
        response = self.client.send_email(
            Source="stanchev2607@gmail.com",
            Destination={
                'ToAddresses': [
                    email,
                ],
            },
            Message={
                'Subject': {
                    'Data': 'Welcome to Stanchev Watches',
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Text': {
                        'Data': 'Enjoy',
                        'Charset': 'UTF-8'
                    },
                    # 'Html': {
                    #     'Data': 'string',
                    #     'Charset': 'string'
                    # }
                }
            },
            # ReplyToAddresses=[
            #     'string',
            # ],
            # ReturnPath='stanchev2607@gmail.com',
            # SourceArn='aws:ses:eu-central-1:850374314577:identity/stanchev2607@gmail.com',
            # ReturnPathArn='string',
            # Tags=[
            #     {
            #         'Name': 'string',
            #         'Value': 'string'
            #     },
            # ],
            # ConfigurationSetName='string'
        )
