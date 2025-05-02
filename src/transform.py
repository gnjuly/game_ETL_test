from pyspark.sql.functions import year, month, countDistinct, to_date

def transform_data(df_kpi):
    '''Transform data to create the users summary and the evolution of the KPI'''

    # Change to date type and add year and month first login columns 
    df_users_summary = df_kpi.withColumn('first_login', to_date('first_login'))\
            .withColumn("first_login_year", year("first_login"))\
            .withColumn('first_login_month', month('first_login'))

    # Create df to analyze first login
    df_evolution = df_users_summary.groupBy(
        "first_login",
        "last_platform",
        "country"
    ).agg(
        countDistinct("user_id").alias("number_of_users")
    )

    return df_users_summary, df_evolution