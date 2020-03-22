import boto3
import logging
from botocore.exceptions import ClientError

'''
For Synchronous Events
'''
class S3Events(object):

    def __init__(self, aws_access_key_id, aws_secret_access_key):

        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.session = boto3.Session(
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
        )
        self.s3 = self.session.resource('s3')

    def upload_fileobj(self, file_name=None, bucket=None, key=None):

        """Upload a file to an S3 bucket
        :param key:
        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :return: True if file was uploaded, else False
        """

        # If S3 object_name was not specified, use file_name
        if (key is None) or (bucket is None):
            logging.info("key and bucket cannot be None")
            return False

        # Upload the file
        s3_client = boto3.client('s3')
        try:
            response = s3_client.upload_fileobj(file_name, bucket, key, ExtraArgs={'ACL': 'public-read'})
        except ClientError as e:
            logging.info("INFO: Failed to upload image")
            logging.error(e)
            return False

        logging.info("File object uploaded to https://s3.amazonaws.com/{}{}".format( bucket, key))
        return True
