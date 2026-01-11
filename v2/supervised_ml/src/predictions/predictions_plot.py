import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, roc_curve, auc
import joblib


### function to verify the split
def verify_split(X_train, X_test, y_train, y_test) : 
    print(f"X_train : {X_train.shape} :: X_test : {X_test.shape} :: y_train : {y_train.shape} :: y_test : {y_test.shape}")


### function to plot the graphs and metrices
def plot_metrices(y_test, y_pred) :

    #-------------metrices
    print(f"Accuracy score : {accuracy_score(y_test, y_pred)}")
    print(f"Confusion matrix : ")
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))


    #--------------graphs
    plt.figure(figsize = (8, 4))
    plt.subplot(1, 2, 1)
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
    
    plt.subplot(1, 2, 2)
    sns.histplot(y_pred, color='purple', bins=len(set(y_pred)))
    plt.title('Predicted Class Distribution')
    plt.xlabel('Predicted Class')
    plt.ylabel('Count')

    plt.tight_layout()
    plt.show()


### function to predict and save the model
def model_predict_test(X_train, X_test, y_train, y_test, model, model_path) :
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    joblib.dump(model, model_path)

    plot_metrices(y_test, y_pred)

 
### function to predict using the best model on the valid data
def best_model_predict_valid(X_valid, best_model_path) :

    best_model = joblib.load(best_model_path)

    y_pred = best_model.predict(X_valid)

    return y_pred 


### function to use other models to predict on the valid data ad compare results with the best model
def other_model_predict_valid(X_valid, y_pred_best, other_model_path) :

    model = joblib.load(other_model_path)

    y_pred = model.predict(X_valid)

    plot_metrices(y_pred_best, y_pred)