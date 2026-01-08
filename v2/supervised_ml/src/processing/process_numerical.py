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

    ts = pd.to_datetime(df[col], errors = 'raise')

    df[f"{col}_year"] = ts.dt.year
    df[f"{col}_month"] = ts.dt.month
    df[f"{col}_day"] = ts.dt.day
    df[f"{col}_hour"] = ts.dt.hour

    return df


### function to distinguish between the dicrete and conitnuous categorical features
def differentiate_discrete_continuous(df) : 

    discrete_cols, continuous_cols = [], []

    for col in df.columns : 
        if (df[col].values.__contains__(0) == True) and (df[col].dtype == 'int64') : 
            discrete_cols.append(col)

        else : 
            continuous_cols.append(col)

    return discrete_cols, continuous_cols