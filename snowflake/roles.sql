CREATE ROLE analytics_role;
GRANT USAGE ON WAREHOUSE analytics_wh TO ROLE analytics_role;
GRANT USAGE ON DATABASE credit_db TO ROLE analytics_role;
