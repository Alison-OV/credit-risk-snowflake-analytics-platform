CREATE TABLE dim_income_band AS
SELECT DISTINCT
income_band
FROM staging.stg_credit_risk;