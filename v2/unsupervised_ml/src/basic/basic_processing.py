import pandas as pd
import numpy as np


### function to load the data from the path given
def load_data(df_path) : 

    df = pd.read_csv(df_path)
    return df


### function to check the nan, duplicates and shape
def check_nan_duplicates_shape(df) : 

    print(f"Shape : {df.shape} \nDuplicates : {df.duplicated().sum()} \n{df.isna().sum()}")


### function to split the data with target feature
def split_target_feature(df, target_feature) : 

    df_new = df.drop(target_feature, axis = 1)
    target_feature = df[target_feature]

    return df_new, target_feature


### function to save the data on the given path provided
def save_data(df, df_path) : 

    df.to_csv(df_path, index = False)