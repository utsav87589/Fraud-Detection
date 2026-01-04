import pandas as pd
import numpy as np


### function to cehck whether we can apply the one hot encoding for the features in a batch
### or they need manual handling
def decide_ohe_strategy(
    df,
    max_categories=10,
    min_class_ratio=0.25
):

    categorical_cols = df.select_dtypes(include=["object", "category"]).columns

    auto_ohe_cols = []
    manual_cols = []

    n_rows = len(df)

    for col in categorical_cols:
        value_counts = df[col].value_counts(normalize=True)
        n_unique = df[col].nunique()

        # criteria for SAFE batch OHE
        if (
            n_unique <= max_categories
            and value_counts.min() >= (min_class_ratio / n_unique)
        ):
            auto_ohe_cols.append(col)
        else:
            manual_cols.append(col)

    return auto_ohe_cols, manual_cols


### function to apply one hot encoding to the categorical features
def one_hot(df, col) : 

    dummies = pd.get_dummies(df[col], dtype = int, prefix = col, prefix_sep = '_', drop_first = True)
    df = pd.concat([df, dummies], axis = 1)

    return df


### function to apply label encoding for the categorical features
def label_encode(df, col, labels) : 

    df = df[col].map(labels)

    return df