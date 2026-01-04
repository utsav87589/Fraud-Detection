### Fraud-Detection : about the project

- Fraud detection is a binary classification problem dataset available on Kaggle. in this problem we have various features available based on which we have to build the model and find out whether the transaction can be labeled as 'fraud' or not.


### about the v2 

- v2 is solving the same dataset but with better structured and organised approach. it covers the limitation of the earlier version aka v1 and enhances the overall quality of the project.

### advantages of v2 : 

- better folder structure
- proper documentation
- introduction of the flowcharts to make the project understandable
- less repititive code
- well balanced notebooks with clean logic inside them
- introduction of gitignore to keep the project clean from rough work


===> Further v2 has divided sections to the dedicated Supervised and Unsupervised ml. for further information please refer to the individual and corresponding folders to learn more about them. each one has the dedicated docs section, which you can access and learn more in detail about the project.


**important** : 

- at some points in the projects I have added the information that either don't exist or it existed but have been modified, now in the first scenario it might be because it is still in the process and I have planned it or it is being tested that's why the information in the docs is there, for the second case I highly recommend to verify the **git history** to see the things.

- for example at the time I have named the files and the folders in the (models) folder of the (supervised_ml) but the models aren't here yet, it's because they are planned ahead to keep up the load for the documenation light and spend less time during the core planning and the naming convention, while doing that particular phase of the project.

**Categorical columns** : 

- Categorical features are handled individually based on cardinality, frequency distribution, and modeling context, rather than applying a uniform encoding strategy.

 Categorical features are profiled first; those with low cardinality and balanced distributions are one-hot encoded in batch, while others are handled individually to prevent sparsity and noise.