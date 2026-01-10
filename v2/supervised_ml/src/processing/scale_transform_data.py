import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import boxcox
from sklearn.preprocessing import MinMaxScaler
import joblib


### function to apply thr boxcox transformation
def apply_boxcox(df, col) : 

    df[col + '_boxcox'], parameter = boxcox(df[col] + 1)


### function to check for the outliers
def check_outliers(df, col) : 

    Q3 = df[col].quantile(0.75)
    Q1 = df[col].quantile(0.25)
    IQR = Q3 - Q1

    return f"Q3 : {Q3} :: Q1 : {Q1} :: min : {df[col].min()} :: max : {df[col].max()} :: extreme upper value {Q3 + 3 * IQR}"


### function to apply the min max scaler and then save it
def apply_scaler(df, scaler_path = None, scaler = None) : 

    cols_to_scale = []

    for col in df.columns : 
        if not (df[col].nunique() <= 2) : 
            cols_to_scale.append(col)

    if (scaler_path is not None) and (scaler is None):

        scaler = MinMaxScaler(feature_range = (0, 1))
        df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])
        joblib.dump(scaler, scaler_path)

    elif (scaler_path is None) and (scaler is not None) : 

            scaler = scaler
            df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])

    return df