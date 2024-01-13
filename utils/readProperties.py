import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\Administrator\\PycharmProjects\\mega\\Config\\config.ini")


class ReadConfig:
    @staticmethod
    def get_aws_access_key_id():
        aws_access_key_id = config.get("aws", "AWS_ACCESS_KEY_ID")
        return aws_access_key_id

    @staticmethod
    def get_aws_secret_access_key():
        aws_secret_access_key = config.get("aws", "AWS_SECRET_ACCESS_KEY")
        return aws_secret_access_key

    @staticmethod
    def get_aws_region():
        aws_region = config.get("aws", "AWS_REGION")
        return aws_region

    @staticmethod
    def get_s3_bucket_name():
        s3_bucket_name = config.get("s3", "S3_BUCKET_NAME")
        return s3_bucket_name

    @staticmethod
    def get_s3_file_name():
        s3_file_name = config.get("s3", "S3_FILE_NAME")
        return s3_file_name
