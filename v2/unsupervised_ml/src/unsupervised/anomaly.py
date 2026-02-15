import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.cluster import DBSCAN


### Function to plot the outliers 
def plot_anomalies(df, outliers) : 
    plt.figure(figsize = (8, 4))
    plt.subplot(1, 2, 1)
    plt.scatter(df[:, 0], df[:, 1])
    plt.scatter(df[outliers, 0], df[outliers, 1], edgecolors = 'r')
    plt.subplot(1, 2, 2)
    plt.scatter(df[:, 0], df[:, 1])
    plt.show()


# ====================== Isolation forest =========================

# function to find the value of contamination
def find_threshold(df) : 

    cif = IsolationForest(contamination = 'auto', random_state = 42)
    cif.fit(df)

    scores = np.sort(cif.score_samples(df))

    print(scores)
    plt.plot(scores)

    return scores


# function to take the value of the scores from the above function and then gives the number of value below that score
def find_contamination(df, scores, threshold) : 

    values = np.where(scores < threshold)
    contamination = 1.0 - ((len(df) - len(values[0])) / len(df))

    print(len(values[0]))
    print(contamination)

#------------function to plot the outliers based on the given value of the contamination
def outliers_isolation_forest(df, contamination) :

    cif = IsolationForest(contamination = contamination, random_state = 42)
    predictions = cif.fit_predict(df)

    outliers = np.where(predictions < 0)

    plot_anomalies(df, outliers)


# ====================== Local outlier factor (LOF) =========================

### for the lof, I consider n_neighbors as 5 and 4, algorithm = 'auto' and leaf_size = 30
### as for the local outliers we wanna detect wuth respect to the closest clusters rather than
### finding out the overall outliers

# function to plot the LOF
def outliers_lof(df, n) : 

    lof = LocalOutlierFactor(n_neighbors = n, algorithm = 'auto', leaf_size = 30)
    predictions = lof.fit_predict(df)

    outliers = np.where(predictions < 1)

    plot_anomalies(df, outliers)


# ====================== DBScan for anomaly detection =========================

### just like for the lof, for dbscan also I considered 2 values of eps,
### one that we got from the clustering by plotting distance indices curve
### second as the default value of 0.1

# function to plot the dbscan for anomaly
def outliers_dbscan(df, eps) : 

    db = DBSCAN(eps = eps)
    predictions = db.fit_predict(df)

    outliers = np.where(predictions < 1)

    plot_anomalies(df, outliers)