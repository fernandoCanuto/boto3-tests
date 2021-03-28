import logging
import boto3
from botocore.exceptions import ClientError


# Indica qual serviço utilizaremos
s3 = boto3.resource('s3')

# Retorna os buckets disponíveis
for bucket in s3.buckets.all():
    print(bucket.name)

# Função para upload de arquivo num bucket especificado
def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# Utilizando a função para upload
upload_file('D:/Desktop/test.csv','bucket-fcanuto')