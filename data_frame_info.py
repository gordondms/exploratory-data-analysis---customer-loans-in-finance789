import pandas as pd

class DataFrameInfo:
    '''
    Class extracts information, statistics and value counts from the DataFrame and its columns
    '''

    def __init__(self, df):
        '''
        Initialising the DataFrameInfo object
        
        Parameters:
        - df (pd.DataFrame): The input DataFrame to be transformed.
        '''
        self.df = df

    def df_column_info(self):
        '''
        Returns summary information about the dataset, including column names and data types
        '''
        return self.df.dtypes   
    
    def df_statistics(self):
        '''
        Returns a statistical summary of the dataset
        '''
        return self.df.describe()

    def df_count_values(self):
        '''
        Returns a count of distinct values in each columns
        '''
        return self.df.nunique()
    
    def df_shape(self):
        '''
        Returns the dataframe shape (number of rows and columns)
        '''
        return self.df.shape
    
    def df_null_count(self):
        '''
        Returns a percentage count of NULL values in each column
        '''
        return self.df.isna().mean() * 100



    