from config import REDSHIFT_HOST, REDSHIFT_PORT, REDSHIFT_DB, REDSHIFT_USER, REDSHIFT_PASSWORD, REDSHIFT_URL
import psycopg2

# SQL commands to create tables in Redshift
CREATE_TABLE_USERS_SUMMARY = """
CREATE TABLE IF NOT EXISTS analytics.users_summary (
    user_id VARCHAR(20) PRIMARY KEY NOT NULL,
    number_logins INT,
    last_platform VARCHAR(10),
    country VARCHAR(3),
    first_login DATE,
    first_login_year INT,
    first_login_month INT
);
"""

CREATE_TABLE_KPI_EVOLUTION = """
CREATE TABLE IF NOT EXISTS analytics.kpi_evolution (
    evolution_id SERIAL PRIMARY KEY,
    first_login DATE,
    last_platform VARCHAR(10),
    country VARCHAR(3),
    number_of_users INT,
);
"""


def create_redshift_tables():
    '''Create Redshift tables if they don't exist in the analytics schema'''

    conn = psycopg2.connect(
        dbname=REDSHIFT_DB,
        user=REDSHIFT_USER,
        password=REDSHIFT_PASSWORD,
        host=REDSHIFT_HOST,
        port=REDSHIFT_PORT
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CREATE SCHEMA IF NOT EXISTS analytics;")
    cur.execute(CREATE_TABLE_USERS_SUMMARY)
    cur.execute(CREATE_TABLE_KPI_EVOLUTION)
    cur.close()
    conn.close()


def load_to_redshift(df, table_name, mode = "overwrite"):
    '''Load Pyspark DataFrame to Redshift table'''

    df.write \
        .format("jdbc") \
        .option("url", REDSHIFT_URL) \
        .option("dbtable", table_name) \
        .option("user", REDSHIFT_USER) \
        .option("password", REDSHIFT_PASSWORD) \
        .mode(mode) \
        .save()