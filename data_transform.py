import pandas as pd


class DataTransform:
    '''
    Class makes changes to the dataframe:
        Data types: integer, dates, and categorical
        Imputing mean and median
    '''
    
    def __init__(self, df):
        '''
        Initialising the DataTransform object
        
        Parameters:
        - df (pd.DataFrame): The input DataFrame to be transformed.
        '''
        self.df = df

    def convert_string_to_integer(self, column):
        '''
        Extracts numbers from a string ("\d+" = one or more of any digit)
        Converts to data type Int64

        Parameters:
        - column: List of colums to be converted

        Returns:
        - pandas.DataFrame
        '''
        self.df[column] = self.df[column].str.extract('(\d+)').astype(float, errors='ignore')
        # self.df[column] = self.df[column].astype('int32')
        return self.df
    
    def convert_to_date(self, column):
        '''
        Converts columns containing dates from object to date format
        
        Parameters:
        - column: List of colums to be converted

        Returns:
        - pandas.DataFrame
        '''
        self.df[column] = pd.to_datetime(self.df[column], format="%b-%Y") 
        return self.df
    
    def convert_to_categorical(self, column):
        '''
        Converts columns containing categorical data to category datatype

        Parameters:
        - column: List of colums to be converted

        Returns:
        - pandas.DataFrame
        '''
        self.df[column] = pd.Categorical(self.df[column])
        return self.df
    
    def impute_mean(df, column):
        ''''
        Impute NULL values with the mean
        
        Parameters:
        - df: pandas.DataFrame
        - column: List of colums to be imputed

        Returns:
        - pandas.DataFrame

        '''
        self.df[column] = self.df[column].fillna(self.df[column].mean())
        return self.df

    def impute_median(df, column):
        ''''
        Impute NULL values with the mean
        
        Parameters:
        - df: pandas.DataFrame
        - column: List of colums to be imputed

        Returns:
        - pandas.DataFrame
        '''
        self.df[column] = self.df[column].fillna(self.df[column].median())
        return self.df
    
