from pyspark.sql import SparkSession
from config import POSTGRES_JDBC_DRIVER
from src.extract import extract_data
from src.transform import transform_data
from src.load import create_redshift_tables, load_to_redshift
from datetime import datetime

def main():
    spark = SparkSession.builder \
            .appName("gamesKPI") \
            .config("spark.jars", POSTGRES_JDBC_DRIVER) \
            .config("spark.hadoop.hadoop.native.io", "false") \
            .getOrCreate()

    # EXTRACT from PostgreSQL
    df_kpi = extract_data(spark)
    print(f"{datetime.now()}: EXTRACT completed successfully")


    # TRANSFORM
    df_users_summary, df_evolution = transform_data(df_kpi)
    print(f"{datetime.now()}: TRANSFORM completed successfully")

    # print("df_users_summary")
    # df_users_summary.show(5)

    # print("df_evolution")
    # df_evolution.show(5)


    # LOAD
    # Create Redshift tables if not exist
    create_redshift_tables()
    # Load data to Redshift
    load_to_redshift(df_users_summary, "user_logins_summary", mode="overwrite")
    load_to_redshift(df_evolution, "daily_logins_summary", mode="append")

    print(f"{datetime.now()}: LOAD completed successfully")


    spark.stop()
    print(f"{datetime.now()}: Pipeline Game_KPI completed successfully")

if __name__ == "__main__":
    main()