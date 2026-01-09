import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stat
import pylab
import seaborn as sns


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



### function to plot the graphs : qq plot, distribution plot and box plot for the continuous columns
def plot_graphs(df, cols) : 

    for col in cols : 

        print(f"column : {col}")

        #---------first plot, which is a hist plot
        plt.figure(figsize = (12, 4))
        plt.subplot(1, 3, 1)
        plt.title('Hist plot')
        df[col].hist()

        #----------second one, which is a qq plot
        plt.subplot(1, 3, 2)
        plt.title('QQ plot')
        stat.probplot(df[col], dist = 'norm', plot = pylab)
        
        #----------third plot, box plot
        plt.subplot(1, 3, 3)
        plt.title('Boxplot')
        sns.boxplot(df[col])

        plt.show()