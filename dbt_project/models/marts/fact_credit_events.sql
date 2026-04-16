SELECT
customer_id,
loan_amount,
credit_score,
default_flag,
CURRENT_TIMESTAMP() AS event_time
FROM {{ ref('stg_credit_risk') }}