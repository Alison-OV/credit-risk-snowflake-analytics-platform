import pandas as pd
import boto3
import os
from botocore.exceptions import NoCredentialsError

# Paths (local simulated S3 structure)
silver_path = "data_lake/silver/credit_risk_clean.csv"
gold_path = "data_lake/gold/credit_risk_analytics.csv"

# Ensure Gold folder exists
os.makedirs(os.path.dirname(gold_path), exist_ok=True)

# Load Silver dataset
df = pd.read_csv(silver_path)

# Create analytics feature (Gold layer logic)
df["income_band"] = pd.cut(
    df["person_income"],
    bins=[0, 30000, 60000, 100000, 999999],
    labels=["low", "medium", "high", "very_high"]
)

# Save locally (simulate S3 Gold)
df.to_csv(gold_path, index=False)

print("Gold dataset created locally. Successfully transformed and saved to:", gold_path)

# Attempt AWS upload if credentials exist
try:
    s3 = boto3.client("s3")

    bucket_name = "fake-gold-bucket"
    s3_key = "gold/credit_risk_analytics.csv"

    s3.upload_file(
        gold_path,
        bucket_name,
        s3_key
    )

    print("Uploaded to AWS S3 Gold layer")

except NoCredentialsError:

    print("AWS credentials not found → running in LOCAL MODE (S3 simulated)")