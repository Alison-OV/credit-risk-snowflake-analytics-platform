from kaggle.api.kaggle_api_extended import KaggleApi
import os

api = KaggleApi()
api.authenticate()

dataset = 'laotse/credit-risk-dataset'

output_path = 'data/bronze'

os.makedirs(output_path, exist_ok=True)

api.dataset_download_files(
    dataset,
    path=output_path,
    unzip=True
)

print('Data downloaded and unzipped successfully.')