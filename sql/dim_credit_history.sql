CREATE TABLE dim_credit_history AS
SELECT DISTINCT
credit_score,
loan_status
FROM staging.stg_credit_risk;