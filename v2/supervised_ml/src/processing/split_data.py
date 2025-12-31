import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


### function to split the data including the target feature for the earliest split possible
def split_data_global(df) : 

    df_train, df_valid = train_test_split(df, test_size = 0.20, random_state = 42)

    df_train = df_train.reset_index(drop = True)
    df_valid = df_valid.reset_index(drop = True)

    return df_train, df_valid


### function to split the data for models i.e. the internal split
def split_data_local(df, target_feature) : 

    X = df.drop(target_feature, axis = 1)
    y = df[target_feature]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42)

    return X_train, X_test, y_train, y_test


### function to split the categorical and numerical columns
# def split_cat_num_cols(df, cols_cat, cols_num) : 
