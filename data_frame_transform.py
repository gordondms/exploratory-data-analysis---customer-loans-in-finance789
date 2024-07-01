import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from data_frame_info import DataFrameInfo as dfi
from scipy import stats


class DataFrameTransform:
    '''
    Class to perform EDA transformations on the data
    '''
    def __init__(self, df):
        '''
        Initialising the DataFrameTransform object
        
        Parameters:
        - df (pd.DataFrame): The input DataFrame to be transformed.
        '''
        self.df = df

    def drop_columns(df, threshold=50):
        '''
        Drop columns with null value count exceeding default threshold (50)
        Calls df_null_count method from DataFrameInfo class in data_frame_info.py
        Identifies the columns to be dropped based on the defined threshold
        Drops identified columns

        Parameters:
        - df: pandas.DataFrame
        - threshold: value defined to provide the null count threshold for dropping columns

        Returns:
        pandas.DataFrame: DataFrame with high null count columns removed.
        '''
        # null_percent = dfi.df_null_count(df)
        # column_drop = dfi.df_null_count[dfi.df_null_count > threshold].index
        # df = df.drop(columns=column_drop)
        # return df
        null_percentage = (df.isnull().sum() / len(df)) * 100
        column_drop = null_percentage[null_percentage > threshold].index
        df = df.drop(columns = column_drop)
        return(df)

    def impute_mean(df, columns):
        '''
        Imputes missing values with the mean for specific columns in the Dataframe
    
        Parameters:
        - df: pandas.DataFrame
        - columns: list of columns for imputing mean

        Returns:
        pandas.DataFrame: DataFrame with values imputed.
        '''
        for column in columns:
            df[column] = df[column].fillna(df[column].mean())
        return df
    
    def impute_median(df, columns):
        '''
        Imputes missing values with the median for specific columns in the Dataframe

        Parameters:
        - df: pandas.DataFrame
        - columns: list of columns for imputing median

        Returns:
        pandas.DataFrame: DataFrame with values imputed.        
        '''
        for column in columns:
            df[column] = df[column].fillna(df[column].median())
        return df
    
    def skew_transform_log(df, columns):
        '''
        Applies skew transformation
        
        Parameters:
        - df: pandas.DataFrame
        - columns: list of columns for skew transformation

        Returns:
        pandas.DataFrame: Skew transformed DataFrame.
        '''
        for column in columns:
            if pd.api.types.is_numeric_dtype(df[column]):
                df[column] = df[column].map(lambda i: np.log1p(i) if i > 0 else 0)
        return df
    
    def skew_transform_boxcox(df, columns):
        '''
        Applies skew transformation

        Parameters:
        - df: pandas.DataFrame
        - columns: list of columns for skew transformation

        Returns:
        pandas.DataFrame: Skew transformed DataFrame.        
        '''
        for column in columns:
            if pd.api.types.is_numeric_dtype(df[column]):
                transform = np.asarray(df[[column]].values)
                df[column] = stats.boxcox(transform)[0]
        return df
    
    def remove_outliers(df, columns):
        '''
        Remove outliers from specific columns in the dataframe

        Parameters:
        - df: pandas.DataFrame
        - columns: list of columns for outlier removal

        Returns:
        pandas.DataFrame: DataFrame after removal of outliers.        
        '''
        for column in columns:
            # Calculate IQR
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1

            # Define boundaries for outliers (applying the Turkey method)
            lower_boundary = Q1 - 1.5 * IQR
            upper_boundary = Q3 + 1.5 * IQR

            # Remove outliers based on calculated boundaries
            df = df[(df[column] >= lower_boundary) & (df[column] <= upper_boundary)]
            return df
                    
                            

