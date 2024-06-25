import pandas as pd

class DataFrameInfo:
    '''
    Class extracts information, statistics and value counts from the DataFrame and its columns
    '''

    def __init__(self, df):
        self.df = df

    def df_column_info(self, df):
        '''
        Returns summary information about the dataset, including column names and data types
        '''
        return self.df.dtypes   
        # return self.df.info()
    
    def df_statistics(self, df):
        '''
        Returns a statistical summary of the dataset
        '''
        return self.df.describe()

    def df_count_values():
        '''
        Returns a count of distinct values in each columns
        '''
        return self.df.nunique()
    
    def df_shape():
        '''
        Returns the dataframe shape (number of rows and columns)
        '''
        return self.df.shape
    
    def df_null_count():
        '''
        Returns a percentage count of NULL values in each column
        '''
        print("Percentage of NULL values in each column:")
        self.df.isna().mean() * 100



    