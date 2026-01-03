### ------------ Folder name : models --------------------

- here is all the information about the 'models' folder including the files and the operation each individual file/subfolder is responsible for, alongside the folder structure.

- in this folder we have the saved models from the training phase, that were tarined on the train data and were tested on the test data and are ready to validate the performance on the valid data.

- there are further 3 subfolders inside the folder : (tree), (distance) and (probablity)


### Subfolder : tree

- it has all the saved tree based models inside that were trained and tested for the tree based data.

- the models are  : 
1. dtc.pkl : Decision tree classifier
2. rfc.pkl : Random forest classifier
3. abc.pkl : Adaboost classifier
4. gbc.pkl : Gradient boost classifier


### Subfolder : distance

- it has the distance based models, that were trained and tested on the distance based data

- the models are : 
1. lr.pkl : Logistic Regression
2. svc.pkl : Support vector classifier
3. knn : KNeighbors classifier


### Subfolder : probablity

- it has the distance based models, that were trained and tested on the tree based data, because the Naive Baye algorithm like the tree based models works on the Raw and Unscaled data as well

- the model is : 
1. nb.pkl : Naive Baye's classification