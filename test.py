import yaml
import psycopg2
import pandas as pd

def load_dict():
    with open('credentials.yaml') as file:
        credentials = yaml.load(file, Loader=yaml.FullLoader)
        print(credentials)

def extract_data(credentials):
        from sqlalchemy import create_engine
        database_type = 'postgresql'
        print(database_type)
        dbapi = 'psycopg2'
        print(dbapi)
        endpoint = credentials['RDS_HOST']
        print(credentials)
        port = credentials['RDS_PORT']
        database = credentials['RDS_DATABASE']
        user = credentials['RDS_USER']
        password = credentials['RDS_PASSWORD']
        engine = create_engine(f"{database_type}+{dbapi}://{user}:{password}@{endpoint}:{port}/{database}")

        engine.connect()

        loan_df = pd.read_sql_query('loan_payments', engine)
        loan_df.head(10)


def main():
    credentials = load_dict()
    print(credentials)
    type(credentials)
    extract_data(credentials)

main()
