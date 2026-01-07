import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


### function to print the count for the different patterns of the entries in the record
def get_format(df, col, patterns) : 

    print(df[col].astype(str).str.len().value_counts())

    for name, pat in patterns.items():
        count = df[col].astype(str).str.match(pat).sum()
        print(name, ":", count)

    

## function to split the feature into more features
def split_col(df, col) : 

    split_df_col = df[col].str.split(sep = ' ', expand = True)
    new_cols = ['Date', 'Time']

    for i in range (split_df_col.shape[1]) : 
        df[f"{col}_{new_cols[i]}"] = split_df_col[i]

    return df