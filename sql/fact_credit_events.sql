CREATE TABLE fact_credit_events AS
SELECT
customer_id,
credit_score,
loan_amount,
default_flag,
CURRENT_DATE() AS date_id
FROM staging.stg_credit_risk;