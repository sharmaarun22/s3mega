from utils.s3_utilities import S3Manager

# Main execution

if __name__ == "__main__":
    s3_manager = S3Manager()

    s3_manager.create_bucket()

    upload_time = s3_manager.upload_file()
    s3_manager.download_file()

    s3_manager.delete_file()

    s3_manager.plot_performance(upload_time)
