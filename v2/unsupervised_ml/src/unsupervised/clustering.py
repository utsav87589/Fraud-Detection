import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
import scipy.cluster.hierarchy as sc
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import silhouette_score


### function to plot the graphs for the clusters and silhouette score as well
def results(df, y_labels) : 

    print(f"Silhouette score : {silhouette_score(df, y_labels)}")

    plt.figure(figsize = (8, 4))
    plt.subplot(1, 2, 1)
    plt.scatter(df[:, 0], df[:, 1], c = y_labels)
    plt.subplot(1, 2, 2)
    plt.scatter(df[:, 0], df[:, 1])
    plt.show()


###------------ Kmeans clustering
### function to find the reight value of the k
def find_k(df) : 

    wcss = []

    for k in range(1, 12) :
        kmeans = KMeans(n_clusters = k, init = 'k-means++')
        kmeans.fit(df)
        wcss.append(kmeans.inertia_)

    print(wcss)
    plt.plot(range(1, 12), wcss)


### function to find the clusters using the value of the k
def clusters_kmeans(df, df_pca,  k) : 

    kmeans = KMeans(n_clusters = k, init = 'k-means++')
    y_labels_kmeans = kmeans.fit_predict(df)

    ### for the results, we are trying to use the clustering for the df but for visualisation, we are using pca data
    print(f"Silhouette score for the full dimensions : {silhouette_score(df, y_labels_kmeans)}")
    results(df_pca, y_labels = y_labels_kmeans)