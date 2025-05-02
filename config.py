import os

# PostgreSQL source
DB_NAME = "your-db-name" 
DB_USER = "your-postgres-user"  
DB_PASSWORD = "your-postgres-password"  
DB_HOST = "localhost"
DB_PORT = "5432"

# Redshift destination
REDSHIFT_HOST = "your-redshift-cluster"
REDSHIFT_PORT = "5439"
REDSHIFT_DB = "your_redshift_db"
REDSHIFT_USER = "your_user"
REDSHIFT_PASSWORD = "your_password"
REDSHIFT_URL = f"jdbc:redshift://{REDSHIFT_HOST}:{REDSHIFT_PORT}/{REDSHIFT_DB}"

# JDBC Driver
POSTGRES_JDBC_DRIVER = os.path.abspath("./drivers/postgresql-42.7.2.jar")