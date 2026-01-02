### ------------ Folder name : Data --------------------

- here is all the information about the data folder, the way folder is structured and the stuff inside each one of them
- Inside the folder we have 5 subfolders, each one contaning different set of files for different purposes
- 5 subfolders : 
1. intermidiate
2. model_ready
3. raw
4. split
5. split_features

- further the subfolders have files inside, at first glance it might look very confusing, but once you get through this readme file, everything will make sense.


==> ***Below the folder are in the sequence** i.e. from the raw we went to the split, then in the split_feature is the data that was processed from the split, similarly the data in the intermidiate came from the split_feature.


##### 1. Subfolder : raw

- contains only 1 file, which is the data in the complete raw form from the Kaggle (no processing and nothing)


### 2. Subfolder : split

- first step towards the featured engineering process
- has three files : train, valid and y_true_valid. the data in this folder is after the first split i.e. separating the valid and train from the raw data inside the (raw) folder

=> train : has all the features (80% of the original data) from the split, later train and test will be made from it to train the models

=> valid : to be used after the model training during the inference phase to evaluate the models on known data and to prevent the data leakage, the target feature was separated from it and stored separately to keep the split clean

=> y_true_valid : target feature from the valid, that was separated, it is saved differently just to verify the things out at the end phase


### 3. Subfolder : split_features

- second step in the data processing, has 4 files : cat_cols_train, num_cols_train, cat_cols_valid, num_cols_valid,
- the idea of this folder is that there are 19 different columns and as we will proceed with the featured engineering, it will be hard to track all of the columns one by one, so the plan was to split all the categorical and numerical columns, then combine them after featured engineering stage.

=> cat_cols_train : has all the categorical columns from train data in the (split) folder

=> num_cols_train : has all the numerical columns from the train data

=> cat_cols_valid : has all the categorical columns from the valid data

=> num_cols_valid : numerical columns from the valid data


### 4. Subfolder : intermidiate

- third step in the data processing, has 6 files : cat_train_processed, num_train_processed, num_train_processed_scaled, cat_valid_processed, num_valid_processed, num_valid_processed_scaled
- in this folder, the data was processed as per the featured engineering logic, where the onehot and label encoding was applied to the categorical columns, transformations, outliers and scaling was done to the numerical columns.

=> cat_train_processed : onehot/label encoded categorical columns from the cat_cols_train

=> num_train_processed : outliers/transformations/split on the numerical columns in the num_cols_train

=> num_train_processed_scaled : outliers/transformations/split + scaled(for the distance based models) on the numerical columns in the num_cols_train

=> cat_valid_processed : onehot/label encoded categorical columns from the cat_cols_valid

=> num_valid_processed : outliers/transformations/split on the numerical columns in the num_cols_valid

=> num_valid_processed_scaled : outliers/transformations/split + scaled(for the distance based models) on the numerical columns in the num_cols_valid


### 5. Subfolder : model_ready

- final step in the data processing before the testing phase, has 4 files : train_tree, train_distance, valid_tree, valid_distance
- in thid folder the data from the intermidiate folder was combined to the correspondant numerical columns dataset to make the data

=> train_tree : cat_train_processed + num_train_processed

=> train_distance : cat_train_processed + num_train_processed_scaled

=> valid_tree : cat_valid_processed + num_valid_processed

=> valid_distance : cat_valid_processed + num_valid_processed_scaled


===> this is all about the data folder in the main project file, if there is confusion please refer to the **flowcharts** to get the more idea about how the split was done and how the data processing was carried out

*** flowcharts ***, at the time you are following the project it is possible that the flowcharts aren't there yet or they have been modified, in tht case, please follow the commit history to get the hint, at the time of writing the docs, I am planning ahead for the project, so the possiblity might be very high.