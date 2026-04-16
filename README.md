# Credit Risk Analytics Platform (Snowflake + dbt + Data Lakehouse)

## Overview

This project use a **modern data engineering architecture** for financial credit risk analytics using:

- Python (ingestion & transformation)
- AWS S3 (Data Lake: Bronze / Silver / Gold)
- Snowflake (Cloud Data Warehouse)
- dbt (Analytics Engineering / transformations)
- Dimensional Modeling (Star Schema)

The dataset is based on a **Credit Risk Benchmark dataset**, commonly used in financial risk modeling.

---

## Architecture
Kaggle Dataset
↓
Python Ingestion Pipeline
↓
AWS S3 Data Lake
(Bronze → Silver → Gold)
↓
Snowflake RAW Layer
↓
dbt Staging Layer
↓
dbt Marts (Star Schema)
↓
BI / Analytics Layer


---

## Data Model

### Star Schema
- fact_credit_events
- dim_customer
- dim_income_band
- dim_credit_history
- dim_time

---

## Data Lake Layers

### Bronze
Raw ingestion from Kaggle (immutable data)

### Silver
Cleaned and standardized dataset:
- null handling
- deduplication
- schema normalization

### Gold
Business-ready dataset:
- income banding
- risk segmentation
- analytics features

---

## Snowflake Layer

- RAW ingestion tables
- optimized warehouse (AUTO_SUSPEND enabled)
- role-based access control (RBAC)
- separation of staging and marts

---

## dbt Layer

### Staging
- data normalization
- type casting
- cleaning logic

### Marts
- star schema implementation
- business-ready fact/dim tables

---

## Key Insights

- Credit score strongly correlates with default risk
- Loan amount increases probability of default
- Income segmentation is a strong predictive feature
- Dataset suitable for regulatory financial modeling

---

## Tech Stack

- Python
- Pandas
- AWS S3
- Snowflake
- dbt
- SQL
- Jupyter Notebooks

---

##  How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run ingestion
python ingestion/kaggle_download.py

# 3. Load to S3
python ingestion/bronze_loader.py

# 4. Transform layers
python ingestion/silver_transform.py
python ingestion/gold_transform.py

# 5. Run dbt
cd dbt_project
dbt run