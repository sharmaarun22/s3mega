import boto3
import time
import os
from utils.readProperties import ReadConfig


class S3Manager:
    def __init__(self, test_data_dir='../Data'):

        self.aws_access_key_id = ReadConfig.get_aws_access_key_id()
        self.aws_secret_access_key = ReadConfig.get_aws_secret_access_key()
        self.aws_region = ReadConfig.get_aws_region()
        self.bucket_name = ReadConfig.get_s3_bucket_name()
        self.file_name = ReadConfig.get_s3_file_name()
        self.test_data_dir = test_data_dir
        self.downloads_dir = "../Downloads"
        self.s3 = boto3.client('s3', aws_access_key_id=self.aws_access_key_id,
                               aws_secret_access_key=self.aws_secret_access_key, region_name=self.aws_region)

    def create_bucket(self):
        try:
            if self.aws_region != 'us-east-1':
                # For regions other than us-east-1, specify the CreateBucketConfiguration
                self.s3.create_bucket(
                    Bucket=self.bucket_name,
                    CreateBucketConfiguration={'LocationConstraint': self.aws_region}
                )
            else:
                # For us-east-1, do not specify CreateBucketConfiguration
                self.s3.create_bucket(Bucket=self.bucket_name)

            print(f"Bucket '{self.bucket_name}' created successfully.")
        except Exception as e:
            print(f"Error creating bucket: {e}")

    def upload_file(self):
        try:
            file_path = os.path.join(self.test_data_dir, self.file_name)
            start_time = time.time()
            self.s3.upload_file(file_path, self.bucket_name, self.file_name)
            upload_time = time.time() - start_time
            print(f"File '{self.file_name}' uploaded successfully. Upload time: {upload_time} seconds.")
            return upload_time
        except Exception as e:
            print(f"Error uploading file: {e}")

    def download_file(self):
        try:
            local_file_path = os.path.join(self.downloads_dir, f"downloaded_{self.file_name}")
            start_time = time.time()
            self.s3.download_file(self.bucket_name, self.file_name, local_file_path)
            download_time = time.time() - start_time
            print(
                f"File '{self.file_name}' downloaded successfully to '{local_file_path}'. Download time: {download_time} seconds.")
            return download_time
        except Exception as e:
            print(f"Error downloading file: {e}")

    def delete_file(self):
        try:
            self.s3.delete_object(Bucket=self.bucket_name, Key=self.file_name)
            print(f"File '{self.file_name}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting file: {e}")

