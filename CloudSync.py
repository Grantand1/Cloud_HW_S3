#Andrew Grant
#Cloud Computing
#The purpose of this assignment is to create a Python program with AWS API.
# The code will update a folder in an S3 bucket with files from a personal computer.

from awscli.clidriver import create_clidriver

class S3_cloud:

    def init_(self, bucket, path, command):
        self.bucket = bucket
        self.path = path
        self.command = command


# AWS S3 bucket and path
bucket = "s3://s3cloudhw"
# Local folder on computer
path = "/Users/andrewgrant 1/Desktop/Hello1"
command = ["s3", "sync", path, bucket, "--delete"]
#connection to the command line
driver = create_clidriver()
# Send the arguments to the aws exectutable file at command line
driver.main(command)
print(command)


