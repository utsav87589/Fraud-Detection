import pandas as pd
import numpy as np


### function to split the categorical and numerical columns from the dataset
### additional logic is for the columns like 'Timestamp' where colum actually belongs to the numerical but ends up in the categorical part
def split_feature(df, force_num = None) : 

    force_num = force_num or []

    df_cat_cols = df.select_dtypes(include = ['object'])
    df_num_cols = df.select_dtypes(include = ['float64', 'int64'])

    for col in force_num : 
        if col in df_cat_cols.columns : 
            df_num_cols[col] = df_cat_cols[col]
            df_cat_cols = df_cat_cols.drop(col, axis = 1)

    return df_cat_cols, df_num_cols