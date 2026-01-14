### ------------ Folder name : notebooks --------------------

- here is all the information about the 'notebooks' folder including the files and the operation each individual file/subfolder is responsible for, alongside the folder structure.

- the notebooks folder is another important folder in the project, which works with the files from the (src) folder, this folder has all the decisions and api calls that processed the whole things.

- although this folder doesn't have any subfolder inside but has many files in it, here in this file I will explain the main purpose of those notebooks files, so if you do follow the documentation for the (src) and flowcharts, you will build a clean and better understanding of the things.

- this folder has a total of 9 different files inside it.


==> 1. file : **************split_data.ipynb****************

- this file processed the Raw data into the split data (i.e. train(80%) and valid (20%)) with the help of (split_data.py) file in the (src folder).


==> 2. file : ****************split_features.ipynb*****************

- this file split the numerical and categorical features for each train and valid data.


==> 3. file : ****************cat_cols.ipynb*****************

- this file process the categorical columns, by checking their unique value and value counts, after it applies the respective onehot and label encoding to the columns, then all the categorical columns are processed properly.


==> 4. file : ****************num_cols_processed.ipynb*****************

- this file process the numerical columns, first it focus on the 'Timestamp' column to make the splits and then it works on the rest by plotting the graphs (qq, hist plot and box plot)


==> 5. file : ****************num_cols_scaled.ipynb*****************

- it has the logic for scaling the numerical columns and saving the scaler object as well.


==> 6. file : ****************model_ready.ipynb*****************

- combining the processed categorical columns with the right processed columns (like 'non-scaled' for the 'tree' based models and 'scaled' for the 'distance' based models), then saving the data in the 'data/model_ready' folder.


==> 7. file : ****************predictions_tree.ipynb*****************

- training, prediction of the tree based models on the train data, saving them and then finding the best model to predict on the valid data. (now for this file it has a special note, as the column : 'Failed_Transaction_Count_7d' was dropped pre prediction, training part from both 'train' and 'valid' data, for the full information please refer to the 'misc.md' file in the docs).


==> 8. file : ****************predictions_distance.ipynb*****************

- training, prediction of the distance based models on the train data, saving them and then finding the best model to predict on the valid data.