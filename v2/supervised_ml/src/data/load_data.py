import pandas as pd
import numpy as np


### function to load the data based on the path given
def load_data(df_path) : 
    df = pd.read_csv(df_path)
    return df


### function to get the nan, shape and the duplicates value inside the dataset
def get_nan_duplicates_shape(df) : 
    print(f"shape : {df.shape} \nduplicate values : {df.duplicated().sum()} \n{df.isna().sum()}")

### function to check the shape only
def get_shape(df) : 
    print(f"{df.shape}")

### function to get the info of the dataset
def get_info(df) :
    return df.info()


### function to get the unique values inside a particular column(s)
def get_unique(df, col) : 
    return df[col].unique()


### function to get the value counts inside of a column(s)
def get_value_counts(df, col) : 
    return df[col].value_counts()


### function to drop the column(s) from the dataset
def drop_col(df, col) : 
    df.drop(col, axis = 1, inplace = True)


### function to save the dataset based on the path given
def save_data(df, df_path) : 
    df.to_csv(df_path, index = False)

