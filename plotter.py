import matplotlib.pyplot as plt
import missingno as msno
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
from statsmodels.graphics.gofplots import qqplot
from matplotlib import pyplot

class Plotter:
    ''''
    Class to visualise insights from the dataset
    '''

    def __init__(self, df):
        self.df = df

    def null_plot(df):
        return msno.matrix(df)

    def measure_skew(df):
        return df.skew(axis = 0, skipna = True, numeric_only = True)
    
    def skewed_columns(column_skew, threshold=1):
        skewed_columns = column_skew[column_skew > threshold].index
        return skewed_columns
    
    def visualise_skews(df, skewed_columns):
        for column in skewed_columns:
            print(column)
            qq_plot = qqplot(df[column] , scale=1 ,line='q', fit=True)
            pyplot.show()

    # def visualise_outliers_boxplot(df):
    #     '''
    #     Visualises outliers using a boxplot
    #     '''
    #     # Columns to plot
    #     numeric_columns = df.select_dtypes(include=['number']).columns
    #     # Create the figure and subplots
    #     fig, axes = plt.subplots(ncols=len(numeric_columns))
    #     # Create the boxplot with Seaborn
    #     for column, axis in zip(numeric_columns, axes):
    #         sns.boxplot(data=df[column], ax=axis) 
    #         axis.set_title(column)
    #         # axis.set(xticklabels=[], xticks=[], ylabel=column)
    #         plt.tight_layout()
    #         plt.show()
    #     # Show the plot
    
    def visualise_outliers_boxplot(df):
        '''
        Visualises outliers using a boxplot
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
        '''
        numeric_columns = df.select_dtypes(include=['number']).columns

        for column in numeric_columns:
            sns.scatterplot(x=df[column][column], y=df_list[column]['Salary'])





    