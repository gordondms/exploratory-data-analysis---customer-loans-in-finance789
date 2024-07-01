import matplotlib.pyplot as plt
import missingno as msno
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
from matplotlib import pyplot
from statsmodels.graphics.gofplots import qqplot


class Plotter:
    ''''
    Class to visualise insights from the dataset
    '''

    def __init__(self, df):
        '''
        Initialising the Plotter object
        
        Parameters:
        - df: pandas.DataFrame: The input DataFrame to be transformed.
        '''
        self.df = df

    def null_plot(df):
        '''
        Plotting null values
        
        Parameters:
        - df: pandas.DataFrame

        Returns:
        - Missingno plot of NaN values
        '''
        return msno.matrix(df)

    def measure_skew(df):
        '''
        Measuring skew

        Parameters:
        - df: pandas.DataFrame

        Returns:
        - Skew calculation
        '''
        return df.skew(axis = 0, skipna = True, numeric_only = True)
    
    def skewed_columns(column_skew, threshold=1):
        '''
        Identifies skewed columns based on a defined threshold

        Parameters:
        - column_skew: List of column skew calculations (from measure_skew function)
        - threshold: Defined threshold for skewness

        Returns:
        - List of skewed columns based on threshold
        '''
        skewed_columns = column_skew[column_skew > threshold].index
        return skewed_columns
    
    def visualise_skews(df, skewed_columns):
        '''
        Visualises the most skewed columns in a QQ plot

        Parameters:
        - df: pandas.DataFrame
        - skewed_columns: List of skewed columns (from skewed_columns function)

        Returns:
        - QQ plot
        '''
        for column in skewed_columns:
            print(column)
            qq_plot = qqplot(df[column] , scale=1 ,line='q', fit=True)
            pyplot.show()

    
    def visualise_outliers_boxplot(df):
        '''
        Visualises outliers using a boxplot

        Parameters:
        - df: pandas.DataFrame
        
        Returns:
        - Boxplot
        '''
        # Columns to plot
        numeric_columns = df.select_dtypes(include=['number']).columns
        # Melt the dataframe to reshape it.
        melted_df = pd.melt(df, value_vars=numeric_columns)
        # Create facet grid
        facet_grid = sns.FacetGrid(melted_df, col="variable",  col_wrap=3, sharex=False, sharey=False)
        facet_grid = facet_grid.map(sns.boxplot, "value", flierprops=dict(marker='x', markeredgecolor='red'))
        return facet_grid
        
    
    def visualise_outliers_scatterplot(df):
        '''
        Visualises outliers using a scatter plot
        
        Parameters:
        - df: pandas.DataFrame
        
        Returns:
        - scatterplot
        '''
        numeric_columns = df.select_dtypes(include=['number']).columns

        for column in numeric_columns:
            sns.scatterplot(x=df[column][column], y=df_list[column]['Salary'])





    