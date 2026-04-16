CREATE TABLE dim_customer AS
SELECT DISTINCT
customer_id,
age,
employment_length
FROM staging.stg_credit_risk;