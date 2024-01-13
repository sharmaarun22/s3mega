from utils.s3_utilities import S3Manager
from utils.visualization_utils import Visualizer


# Main execution
if __name__ == "__main__":
    s3_manager = S3Manager()

    s3_manager.create_bucket()

    upload_time = s3_manager.upload_file()
    s3_manager.download_file()

    s3_manager.delete_file()

    visualizer = Visualizer()
    visualizer.plot_performance(upload_time)
