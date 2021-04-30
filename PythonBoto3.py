import boto3
bucket_name = 'eng84-jordan-boto3'
file_name = 'README.md'
s3 = boto3.resource('s3')

def create_bucket():
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})

def upload_file():
    s3.Bucket(bucket_name).upload_file(Filename=file_name, Key=file_name)

def download_file():
    s3.Bucket(bucket_name).download_file(Filename=file_name, Key=file_name)

def delete_file():
    s3.Object(bucket_name, file_name).delete()

def delete_bucket():
    s3.Bucket(bucket_name).delete()

def display_buckets():
    for bucket in s3.buckets.all():
        print(bucket.name)

if __name__ == "__main__":
    # create_bucket()
    # upload_file()
    # download_file()
    # delete_file()
    # delete_bucket()
    # display_buckets()
    pass