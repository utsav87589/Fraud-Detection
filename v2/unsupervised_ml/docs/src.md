### ------------ Folder name : src --------------------

- here is all the information about the data folder, the way folder is structured and the stuff inside each one of them.

- src folder have the functions written inside that were used in the notebook files to replace the part of writing the same logic across the different files, when it can simple be put down into the src files where we simple call the functions across mutiple files and making the code look easier and more manageable.

- in the src folder, we have 2 subfolders :

1. basic : in this subfolder we have one file (basic_processing.py) with the following information inside
- load_data(df_path) : loads the data
- check_nan_duplicates_shape(df) : check for the nan, duplicates and the shape of the dataset (all at once)
- split_target_feature(df, target_feature) : split the target feature from the dataset (we don't need the target feature incase of unsupervised ML)
- save_data(df, df_path) : save the data, (after we split or change the name or anything)


2. unsupervised : here we have 3 files : 

1. pca.py : 
- get_variance(df) : get the variance of the dataset before we compress the dataset to 2 dimensions using the pca in order to check the diveristy in between the features.
- reduce_dimensions(df) : reduce the dimensions of the dataset (always to 2 for the visualisation purpose)
- check_shape(df) : check only the shape of the dataset (obviously after the pca, we cannot check the nan and other things, as they would be unnecessary at this point)

2. clustering.py : 
- 