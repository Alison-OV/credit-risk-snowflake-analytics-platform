import pandas as pd
import boto3
import os
import shutil
from botocore.exceptions import NoCredentialsError

# Paths
bronze_path = "data_lake/bronze/credit_risk_dataset.csv"
silver_path = "data_lake/silver/credit_risk_clean.csv"

# Ensure silver folder exists
os.makedirs(os.path.dirname(silver_path), exist_ok=True)

# Load Bronze dataset
df = pd.read_csv(bronze_path)

# Transformations (Silver layer cleaning)
df.columns = df.columns.str.lower()
df = df.drop_duplicates()
df = df.fillna(0)

# Save locally (simulate S3 Silver)
df.to_csv(silver_path, index=False)

print("Silver dataset created locally. Successfully transformed and saved to:", silver_path)

# Try uploading to AWS S3 if credentials exist
try:
    s3 = boto3.client("s3")

    bucket_name = "fake-silver-bucket"
    s3_key = "silver/credit_risk_clean.csv"

    s3.upload_file(
        silver_path,
        bucket_name,
        s3_key
    )

    print("Uploaded to AWS S3 Silver layer")

except NoCredentialsError:

    print("AWS credentials not found → running in LOCAL MODE (S3 simulated)")