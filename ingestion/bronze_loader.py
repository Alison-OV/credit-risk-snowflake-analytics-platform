import os
import shutil
import boto3
from botocore.exceptions import NoCredentialsError

file_path = "data/bronze/credit_risk_dataset.csv"
local_bucket = "data_lake/bronze/credit_risk_dataset.csv"

try:
    s3 = boto3.client("s3")
    
    s3.upload_file(
        file_path,
        "fk-bronze-bucket",
        "bronze/credit_risk_dataset.csv"
    )

    print("Uploaded to AWS S3")

except NoCredentialsError:

    os.makedirs(os.path.dirname(local_bucket), exist_ok=True)
    shutil.copy(file_path, local_bucket)

    print("AWS not configured → saved locally instead")