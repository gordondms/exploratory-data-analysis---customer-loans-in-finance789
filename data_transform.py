import pandas as pd


class DataTransform:
    '''
    Class corrects the datatype for specific columns within the dataframe
    '''
    
    def __init__(self, df):
        self.df = df

    def convert_string_to_integer(self, columns):
        '''
        Extracts numbers from a string ("\d+" = one or more of any digit)
        Converts to data type Int64
        '''
        self.df[columns] = self.df[columns].str.extract('(\d+)')
        self.df[columns] = self.df[columns].astype('int64')
        return self.df
    
    def convert_to_date(self, columns):
        '''
        Converts columns containing dates from object to date format
        '''
        self.df[columns] = pd.to_datetime(self.df[columns], format="%b-%Y") 
        return self.df
    
    def convert_to_categorical(self, columns):
        '''
        Converts columns containing categorical data to category datatype
        '''
        self.df[columns] = pd.Categorical(self.df.[columns])
        return self.df
    
