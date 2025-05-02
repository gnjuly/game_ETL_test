import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

def create_database():
    '''Create PostgreSQL database if it doesn't exist'''

    # Connect to PostgreSQL server
    conn = psycopg2.connect(
        dbname="postgres",
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    # Create database if it doesn't exist
    try:
        cur.execute(f"CREATE DATABASE {DB_NAME};")
        print(f'Database {DB_NAME} created successfully')
    except psycopg2.errors.DuplicateDatabase:
        print(f'Database {DB_NAME} already exists')
 
    cur.close()
    conn.close()

def create_tables_and_insert_data():
    '''Create tables and insert data into PostgreSQL database'''

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()

    # Create tables
    cur.execute("""
    DROP TABLE IF EXISTS logins;
    CREATE TABLE logins (
        id BIGSERIAL PRIMARY KEY NOT NULL,
        user_id VARCHAR(20),
        login_ts TIMESTAMP
    );
    """)

    cur.execute("""
    DROP TABLE IF EXISTS users_info;
    CREATE TABLE users_info (
        user_id VARCHAR(20) PRIMARY KEY NOT NULL,
        android BOOLEAN DEFAULT FALSE NOT NULL,
        ios BOOLEAN DEFAULT FALSE NOT NULL,
        last_login TIMESTAMP(6) NOT NULL,
        other BOOLEAN DEFAULT FALSE NOT NULL
    );
    """)

    cur.execute("""
    DROP TABLE IF EXISTS users_country;
    CREATE TABLE users_country (
        user_id VARCHAR(20) PRIMARY KEY NOT NULL,
        continent VARCHAR(3),
        country VARCHAR(3)
    );
    """)

    # Insert data in logins table
    cur.execute("""
    INSERT INTO logins (user_id, login_ts) VALUES
    ('user1', '2025-04-20 10:00:00'),
    ('user1', '2025-04-21 11:00:00'),
    ('user2', '2025-04-22 15:00:00'),
    ('user3', '2025-04-23 18:00:00'),
    ('user2', '2025-04-23 16:00:00'),
    ('user4', '2025-04-25 20:00:00'),
    ('user5', '2025-04-26 14:00:00'),
    ('user6', '2025-04-26 17:00:00');
    """)

    # Insert data in users_info table
    cur.execute("""
    INSERT INTO users_info (user_id, android, ios, last_login, other) VALUES
    ('user1', FALSE, TRUE, '2025-04-21 11:00:00', FALSE),
    ('user2', TRUE, FALSE, '2025-04-23 16:00:00', FALSE),
    ('user3', FALSE, FALSE, '2025-04-23 18:00:00', TRUE),
    ('user4', FALSE, TRUE, '2025-04-25 20:00:00', FALSE),
    ('user5', TRUE, FALSE, '2025-04-26 14:00:00', FALSE),
    ('user6', FALSE, FALSE, '2025-04-26 17:00:00', TRUE);
    """)

    # Insert data in users_country table
    cur.execute("""
    INSERT INTO users_country (user_id, continent, country) VALUES
    ('user1', 'SRR', 'ARG'),
    ('user2', 'SRR', 'CHL'),
    ('user3', 'NNN', 'CAN'),
    ('user4', 'EEE', 'ESP'),
    ('user5', 'NNN', 'USA'),
    ('user6', 'NNN', 'MEX');
    """)

    conn.commit()

    cur.close()
    conn.close()


create_database()
create_tables_and_insert_data()
print("Database and tables created successfully, and data inserted")