# s3mega
**Automate AWS S3 tasks with Python**

This project provides a Python script for automating various tasks with AWS S3, including creating an S3 bucket, uploading a text file, downloading the file, and generating performance reports. The code follows best practices, encapsulating functionality into an object-oriented structure, and separating configuration, utility files, automation scripts, and reports into organized directories.

**Features:**

* Create an AWS S3 bucket
* Upload a text file to the S3 bucket
* Download the text file from the S3 bucket
* Delete the text file from the S3 bucket
* Generate a performance report for file uploads

**Directory Structure:**

* Config: Contains configuration details in the config.ini file.
* utils: Houses the S3Manager class for S3 automation.
* scripts: Includes the main execution script main_script.py.
* Reports: Stores generated performance reports.
* Data: Holds test data files (e.g., test.txt).
* Downloads: Destination directory for downloaded files.

**Usage:**

* clone the repository
* install requirements using:
pip install -r requirements

* Set up your AWS credentials and configuration in the Config/config.ini file. 
* Place the file to be uploaded in the Data directory. 
* Run main_script.py from the scripts directory.

**Dependencies:**

* Python 3.x
* Boto3 library
* Matplotlib library
