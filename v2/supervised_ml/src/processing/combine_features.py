import pandas as pd
import numpy as np


### function to combine the features and return the data
def combine_features(feature_cat, feature_num) : 

    df = pd.concat([feature_cat, feature_num], axis = 1)

    return df