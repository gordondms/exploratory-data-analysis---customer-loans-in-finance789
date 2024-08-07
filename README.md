# Project Title: Exploratory-Data-Analysis---Customer-Loans-in-Finance789

## A description of the project: what it does, the aim of the project, and what you learned
This project is focused on performing exploratory data analysis on a loan portfolio.  It utilises various statistical and data visualisation techniques to uncover patterns, relationships, and anomalies in the loan data.  The intention is to uncover information that will enable the business to make more informed decisions about loan approvals, pricing, and risk management. 

The project starts with the development of a Python script that creates a class and associated methods to:
- Load a dictionary from a local YAML file that contains the credentials to access an AWS RDS database
- Access the AWS RDS database
- Extract a table from that database as a dataframe
- Save the table to a local CSV file
- Load a dataframe from the local CSV file

The project then works though the fundamental steps in EDA:
- Converting the columns to the correct format
- Creating a class to get information from the DataFrame
- Removing or imputing missing values in the data
- Performing transformations on skewed columns
- Removing outliers from the data
- Dropping overly correlated columns

Key learnings included:
- Practical implementation of the theory that was covered in the lessons
- Understanding the detailed code/syntax required for different steps
- Reinforcing the value of creating reusable classes for key steps
- Highlighting that it is not always a clear-cut decision regarding dropping data/columns or correlation
- Different approaches to data analysis and visualisation


## Installation instructions
N/A
## Usage instructions

### The EDA.ipynb file provides all the information and key steps undertaken during this project.
### The Analysis.ipynb file provides a summary of the analysis steps undertaken 

## File structure of the project

The key files are:

-  db_utils.py - This is the primary Python script file
-  load_data.csv - Local data file (saved from the Python script)
-  credentials.yaml - This is the YAML file that contains the credentials to access the AWS database
-  .gitignore - This file references the YAML file that contains the credentials to access the AWS database
-  data_frame_info.py - This contains a Class (DataFrameInfo) that extracts information, statistics and value counts from the DataFrame
-  data_transform.py - This contains a Class (DataTransform) that makes changes to the dataframe, including datatype and imputing mean/median values.
-  data_frame_transform.py - This contains a Class (DataFrameTransform) that performs EDA transformation on the data
-  plotter.py - This contains the Class (Plotter) that visualises insights from the dataset
-  EDA-ipynb - This Jupyter file provides an overview of the project and the key steps in terms of data extraction, data changes, transformations and visualisation
-  Analysis.ipynb - This Jupyter file provides a summary of the analysis and visualisation of the loans data

## License information
N/A
