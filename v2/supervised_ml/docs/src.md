### ------------ Folder name : src --------------------

- here is all the information about the 'src' folder including the files and the operation each individual file/subfolder is responsible for, alongside the folder structure.

- (src) folder conatins all our reusable and core functions that were used in with the combined logic in the (notebooks) files to make the project.

- this folder further has 3 subfolders : 
1. data
2. predictions
3. processing

- further, inside each subfolder has __init__.py file common in all of them, which is responsible to help with the exports of those functions, further, they have different files, each one with their unique purpose which is explained in this readme file (src.md).

- for more clarification please feel free to refer to either on of the following : (flowcharts) or the (individual) files inside the folder (src).


### Subfolder : data

- contains (__init__.py) and (data.py) files, main logic of code inside this folder is to load the data, apply some initial checks like checking the nan values, veryfying the shapes, dropping the cols or saving the data.


==> file : **load_data.py** : 

1. load_data(df_path) : loads the dataset based on the given path

2. get_shape(df) : get the shape of the dataset

3. get_nan(df) : gives the nan values inside the dataset

4. get_info(df) : gives the info about the columns like : dtype, length of the cols etc.

5. get_unique(df, col) : returns the unique values inside the column

6. get_value_counts(df, col) : gives the value counts for the categories inside the particular column(s)

7. drop_col(df, col) : drop the particular column from the dataset

8. save_data(df, df_path) : saves the dataset to the given path


### Subfolder : processing

- this is one of the core subfolder inside the src folder, the logic inside is responsible from everything all the way from splitting the data to the encodings/scaling/transformations i.e. to make the data model ready starting from the raw data, it has **3** files at the time of writing this documentation, but that numbers will be keep changing (please refer to the git history to see more info in this regard).
- it has (__init__.py), (split_data.py) and (split_features.py) files inside of it.


==> file : **split_data.py** : 

1. split_data_global(df) : split the data in train(80%) and valid data(20%) as a aresult of the earliest cleanest split so that the valid data act as a complete new data during the model inference phase.

2. split_data_local(df, target_feature) : split the data (only used for the train data though) into train and test data (train/test split) to train the models.


==> file : **split_feature**

1. split_feature(df, force_num = None) : splites the numerical columns and the categorical columns from the dataset, the parameter (force_num) helps determining the folder which are categorical by the type but in reality they are numerical in nature (eg : Timestamp)


==> file : **process_numerical.py**

1. get_format(df, col, patterns) : gives the value counts for the specific pattern of the specific column (for the Timestamp column, to give us the different number of formats)

2. split_col(df, col) : splits the column around a particular operator by converting into the date and time format (exclusively for the Time stamp column)

3. differentiate_discrete_continuous(df) : differentiate between the discrete(non scaling) and continuous (scaling) numerical columns.