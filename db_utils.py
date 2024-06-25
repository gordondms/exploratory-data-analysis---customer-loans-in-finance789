import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import yaml

# Creating new class containing the methods to extract data from the RDS database

class RDSDatabaseConnector:

    def __init__(self, credentials):
        self.credentials = self.load_dict()

    def load_dict(self):
        with open('credentials.yaml') as file:
            credentials = yaml.load(file, Loader=yaml.FullLoader)
            print(credentials)
            return credentials

    def load_data(self):
        '''
        Loading data from AWS RDS utilising a SQLAlchemy engine.
        Utilises credentials extracted from load_dict.
        '''    
        database_type = 'postgresql'
        dbapi = 'psycopg2'
        endpoint = self.credentials['RDS_HOST']
        port = self.credentials['RDS_PORT']
        database = self.credentials['RDS_DATABASE']
        user = self.credentials['RDS_USER']
        password = self.credentials['RDS_PASSWORD']
        engine = create_engine(f"{database_type}+{dbapi}://{user}:{password}@{endpoint}:{port}/{database}")
        engine.connect()
        return engine

    
    def extract_table(self):
        '''
        Extraction of data table from RDS database.
        Data table is returned as a DataFrame
        '''
        loan_df = pd.read_sql_query('SELECT * FROM loan_payments', con=engine)
        #print(loan_df.head(40))
        pd.set_option('display.max_columns', None)
        loan_df.head(40)
        return loan_df
    
    def save_table(self, loan_df, CSV_filename):
        '''
        DataFrame saved to local CSV file.
        '''
        loan_df.to_csv(CSV_filename)
    
    def load_df(self, filename):
        '''
        Local CSV file being loaded as a Pandas DataFrame
        '''
        loansfile_df = pd.read_csv(filename)
        loansfile_df.info()
        print(loansfile_df.shape)
        print(loansfile_df.head(10))

   


# Function to load AWS credentials stored in a YAML file

def load_dict(filename):
    with open(filename) as file:
        credentials = yaml.load(file, Loader=yaml.FullLoader)
        print(credentials)
        return credentials



if __name__ == '__main__':
    credentials = load_dict('credentials.yaml')
    connection = RDSDatabaseConnector(credentials)
    engine = connection.load_data()
    connection.load_data()
    loan_df = connection.extract_table()
    connection.save_table(loan_df, 'loan_data.csv')
    connection.load_df('loan_data.csv')

print("percentage of missing values in each column:")
print(loan_df.isna().mean() * 100)