import matplotlib.pyplot as plt
import os


class Visualizer:

    def __init__(self, reports_dir="../Reports"):
        self.reports_dir = reports_dir

    def plot_performance(self, upload_time):
        labels = ['Upload']
        times = [upload_time]

        plt.bar(labels, times, color=['blue'])
        plt.xlabel('Operation')
        plt.ylabel('Time (seconds)')
        plt.title('S3 File Upload Performance Report')

        # Save the report in the Reports directory
        report_path = os.path.join(self.reports_dir, 'upload_performance_report.png')
        plt.savefig(report_path)

        print(f"Upload performance report saved to '{report_path}'.")

