import pandas as pd
import numpy as np
from sklearn.decomposition import PCA


### function to check the variance ratio 
def get_variance(df) : 

    pca = PCA()
    pca.fit_transform(df)

    arr = np.array(pca.explained_variance_ratio_)
    np.set_printoptions(suppress = True)

    return arr


### function to reduce the dimensons to 2 for the clustering and anomaly detection
def reduce_dimensions(df) : 

    pca = PCA(n_components = 2)
    df_pca = pca.fit_transform(df)
    return df_pca


### function to verify the shape
def check_shape(df) : 
    return df.shape