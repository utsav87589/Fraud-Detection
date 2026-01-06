import pandas as pd
import numpy as np


### function to give us the n_unique values, class ratio, later in notebook file we decide whether to do batch encoding or individual
def cat_summary(df) : 

    summary_cols = {}

    for col in df.columns  : 

        ### this logic has already been mentioned in another src file, but that was for the earlier stages of the project

        summary_cols[col] = {
            'n_unqiue' : df[col].nunique(),
            'value_counts' : df[col].value_counts()
        }

    return summary_cols



### function to apply one hot encoding to the categorical features, (assuming we separated the categorical columns earlier)
def one_hot(df) : 

    for col in df.columns : 

        dummies = pd.get_dummies(df[col], dtype = int, prefix = col, prefix_sep = '_', drop_first = True)
        df = pd.concat([df, dummies], axis = 1)

        df = df.drop(col, axis = 1)

    return df


### function to apply label encoding for the categorical features
def label_encode(df, col, labels) : 

    df = df[col].map(labels)

    return df