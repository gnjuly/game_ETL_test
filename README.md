# OBJECTIVE

This project performs an ETL (Extract, Transform, Load) process to move and prepare game login data from a PostgreSQL database into Amazon Redshift, with the goal of enabling KPI analysis by data analysts.

- Extract data from the PostgreSQL source.
- Transform the data using PySpark.
- Create analytics tables in Redshift if they don't exist.
- Load the transformed data into Redshift.


## Requirements

- Python 3.10
- PostgreSQL
- Amazon Redshift

## Steps to run

1. Clone respository

2. Create a virtual environment

WINDOWS - PYTHON 3.10.4

py -m virtualenv -p python3.10.4 virtual_env

.\virtual_env\Scripts\Activate

py -m pip install -r requirements.txt


3. Complete data configutation

In config.py complete data configuration

4. Run code

py run.py