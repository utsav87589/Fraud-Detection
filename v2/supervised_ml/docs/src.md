### ------------ Folder name : src --------------------

- here is all the information about the 'src' folder including the files and the operation each individual file/subfolder is responsible for, alongside the folder structure.

- (src) folder conatins all our reusable and core functions that were used in with the combined logic in the (notebooks) files to make the project.

- this folder further has 3 subfolders : 
1. data
2. predictions
3. processing

- further, inside each subfolder has __init__.py file common in all of them, which is responsible to help with the exports of those functions, further, they have different files, each one with their unique purpose which is explained in this readme file (src.md).

- for more clarification please feel free to refer to either on of the following : (flowcharts) or the (individual) files inside the folder (src).


### ====================Subfolder : data===========================

- contains (__init__.py) and (data.py) files, main logic of code inside this folder is to load the data, apply some initial checks like checking the nan values, veryfying the shapes, dropping the cols or saving the data.


==> file : *******************load_data.py*****************

1. load_data(df_path) : loads the dataset based on the given path

2. get_shape(df) : get the shape of the dataset

3. get_nan(df) : gives the nan values inside the dataset

4. get_info(df) : gives the info about the columns like : dtype, length of the cols etc.

5. get_unique(df, col) : returns the unique values inside the column

6. get_value_counts(df, col) : gives the value counts for the categories inside the particular column(s)

7. drop_col(df, col) : drop the particular column from the dataset

8. save_data(df, df_path) : saves the dataset to the given path


###  ====================Subfolder : processing=====================

- this is one of the core subfolder inside the src folder, the logic inside is responsible from everything all the way from splitting the data to the encodings/scaling/transformations i.e. to make the data model ready starting from the raw data, it has **3** files at the time of writing this documentation, but that numbers will be keep changing (please refer to the git history to see more info in this regard).
- it has (__init__.py), (split_data.py) and (split_features.py) files inside of it.


==> file : *******************split_data.py******************* 

1. split_data_global(df) : split the data in train(80%) and valid data(20%) as a aresult of the earliest cleanest split so that the valid data act as a complete new data during the model inference phase.

2. split_data_local(df, target_feature) : split the data (only used for the train data though) into train and test data (train/test split) to train the models.


==> file : ***********************split_feature***********************

1. split_feature(df, force_num = None) : splites the numerical columns and the categorical columns from the dataset, the parameter (force_num) helps determining the folder which are categorical by the type but in reality they are numerical in nature (eg : Timestamp)


==> file : ***********************process_categorical.py***********************

1. cat_summary(df) : return the unique values and value count for the numerical columns

2. def one_hot(df) : apply one hot encoding to the categorical column(s) (in this dataset, the onehot encoding was applied at once to all categorical features)

3. label_encode(df, col, labels) : apply the label encoding to the column (never been used in this dataset)


==> file : ***********************process_numerical.py***********************

1. get_format(df, col, patterns) : get the all different date-time format for different entries in the dataset. (only used for the 'Timestamp' column)

2. split_col(df, col) : split the timestamp column into different separate records (like hour, minute etc.) (only used for the 'Timestamp' column)

3. plot_graphs(df, cols) : plot the hist plot, qq plot and box plot for the numerical columns

4. plot_graphs_post_scaling(df, df_copy) : plot the graphs for the numerical columns, pre scaling and post scaling for the comparison and cross verification purposes.


==> file : ***********************scale_transform_data.py***********************

1. apply_boxcox(df, col) : apply the boxcox transformation to the column.

2. check_outliers(df, col) : check the outliers for a specific column (based on the first, third quantile, IQR and min, max values)

3. apply_scaler(df, scaler_path = None) : apply the scaler to the nuemrical column(s), and save the scaler object to the given path or load the scaler object which is trained already and use it for another data.


==> file : ***********************combine_feature.py***********************

1. combine_features(feature_cat, feature_num) : combines the different columns to form main dataset, it was used for the tree and distance based data, after the processing on the categorical and the numerical columns was done separatelty.


###  ====================Subfolder : predictions=====================

- in this folder, we have all the files that have the functions to work on the 'model_ready' data, which includes veryfying the split, plot the metrices, saving the models and making the predictions.

- this folder has only 2 files in it : (__init__.py and predictions_plot.py).


==> file : ***********************predictions_plot.py***********************

1. verify_split(X_train, X_test, y_train, y_test) : validate the split of the data after train-test split by checking their shape,

2. plot_metrices(y_test, y_pred) : plot the graphs and metrices for the comparison of the y_pred (predicted data) and y_test(true data) to see the model performance, this function has never been called of extrenally, always used internally with other functions.

3. model_predict_test(X_train, X_test, y_train, y_test, model, model_path) : train the models and then predict on the test data, then save those models. (test data is the one we have after the split from train-test split).

4. best_model_predict_valid(X_valid, best_model_path) : after finding out the best model based on the graphs and metrices, this function use the same trained best model to predict on the valid data and then return those predictions to see how close the other models perform with respect to the best model prediction on the valid data. (for 'trees' it was 'Random forest classifier' and for 'distance' based models it was 'SVC').

5. other_model_predict_valid(X_valid, y_pred_best, other_model_path) : load the other models that are pre trained already on training data and then make the predictions on the valid data, but this time the metrices and performances are verified with respect to the best model.