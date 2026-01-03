### ------------ Folder name : notebooks --------------------

- here is all the information about the 'notebooks' folder including the files and the operation each individual file/subfolder is responsible for, alongside the folder structure.

- the notebooks folder is another important folder in the project, which works with the files from the (src) folder, this folder has all the decisions and api calls that processed the whole things.

- although this folder doesn't have any subfolder inside but has many files in it, here in this file I will explain the flow of those notebooks files, so if you do follow the documentation for the (src) and flowcharts, you will build a clean and better understanding of the things.


==> file : **split_data.ipynb**

- this file processed the Raw data into the split data (i.e. train(80%) and valid (20%)) with the help of (split_data.py) file in the (src folder).

- the main flow of the file follows as  : 

1. setup the autoreloader -->

2. setup the system path, imported the function from the src file -->

3. setup the data path -->

4. loaded the data -->

5. check the shape, nan values and info for the dataset -->

6. get the value_count for the target feature (fraud label) : to check the balance of the classes and need of the smote -->

7. check the values_count for the transaction_id and user_id columns, then drop those columns --> 

8. verified the shape again -->

9. split the data into train and valid data -->

10. verified the train data -->

11. verified the valid data, drop and stored the target feature : fraid_label independently -->

12. setup the path for each valid, train and y_true_valid -->

13. saved them at the respective paths and reloaded them again to verify.


==> file : **split_data.ipynb**

- this file spliteed the numerical and categorical features for each train and valid data.

- the main flow of the file follows as  : 

1. setup the autoreloader, system path and imported the functions from the src --> 

2. setup the data path(for the train data and valid both), loaded the data(train only), verified the nan and the shape -- >

3. made the split into cat_cols_train and num_cols_train (with force_num = 'Timestamp) -->

4. verified those splits using the shape and df.head() -->

5. loaded the data(valid data), verified the nan and the shape -->

6. made the split into cat_cols_valid and num_cols_valid (with force_num = 'Timestamp) -->

7. verified those splits using the shape and df.head() -->

8. setup the path for those feature split data -->

9. saved them to the corresponding locations -->

10. verified the things by loading them again.