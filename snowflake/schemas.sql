CREATE SCHEMA raw;
CREATE SCHEMA staging;

CREATE SCHEMA marts;

CREATE TABLE raw.credit_risk_raw (
customer_id STRING,
age INT,
income FLOAT,
loan_amount FLOAT,
credit_score INT,
employment_length INT,
loan_status STRING,
default_flag INT
);

PUT file://credit_risk_dataset.csv @raw_stage;

COPY INTO raw.credit_risk_raw
FROM @raw_stage
FILE_FORMAT = (TYPE = CSV FIELD_OPTIONALLY_ENCLOSED_BY='"');
