from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

def extract_data(spark):
    '''Extract the necessary data from PostgreSQL database'''

    # Query to extract data from DDBB 
    query_kpi = """
                SELECT
                    l.user_id,
                    COUNT(l.id) AS number_logins,
                    CASE
                        WHEN ui.android THEN 'ANDROID'
                        WHEN ui.ios THEN 'IOS'
                        WHEN ui.other THEN 'OTHER'
                        ELSE 'UNKNOWN'
                    END AS last_platform,
                    uc.country,
                    MIN(l.login_ts) AS first_login
                FROM logins AS l
                LEFT JOIN users_info AS ui ON l.user_id = ui.user_id
                LEFT JOIN users_country AS uc ON l.user_id = uc.user_id
                GROUP BY l.user_id, ui.android, ui.ios, ui.other, uc.country
                """

    # Extract data
    df_kpi = spark.read \
            .format("jdbc") \
            .option("url", f"jdbc:postgresql://{DB_HOST}:{DB_PORT}/{DB_NAME}") \
            .option("dbtable", f"({query_kpi}) as tmp") \
            .option("user", DB_USER) \
            .option("password", DB_PASSWORD) \
            .option("driver", "org.postgresql.Driver") \
            .load()

    print("FINISH Extract data")
    return df_kpi