

#Load Iris dataset
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
#loading the iris data
iris = load_iris()
print(iris.feature_names)
iris.data
print(iris.target_names)
iris.target
#target varibale and the label names of 0,1,2

print(iris.target)
#target variable
#0 = setosa, 1 = versicolor, 2 = virginica.
np.bincount(iris.target)

#Split into train/test (80/20)

X=iris.data
#all independent variables
Y=iris.target
#targe variable

Xtrain,Xtest,Ytrain,Ytest=train_test_split(X,Y,test_size=0.2,random_state=65)

print(Xtrain.shape)
print(Xtest.shape)
print(Ytrain.shape)
print(Ytest.shape)



#Train a simple classifier (Decision Tree or Logistic Regression)

clf = LogisticRegression(max_iter=200)
clf.fit(Xtrain, Ytrain)
#using training data with independent variables to train the model with solution provided
#it will learn the pattern of data and learn the weights of variables
print(clf.coef_)
#we have 3 class for target varibales : 'setosa' 'versicolor' 'virginica
# 3 equations : one for each species
#this will give the probability for each species and the one with the high probability will get the label for that row.
print(clf.intercept_)
# 3 intercepts
#once the equations is solved then probability for each class is calculated
#the one with the highest probabiity is picked and that is the label for that row


#Make predictions and calculate accuracy

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

y_pred = clf.predict(Xtest)
accuracy = accuracy_score(Ytest, y_pred)

accuracy
#96% accuracy


#Visualize decision boundaries (for 2 features)

#Confusion matrix
#Precision, Recall, F1-score
#ROC curve and AUC
#Cross-validation scores (5-fold)
#Compare performance on train vs test set (check for overfitting)

from sklearn.metrics import (
    confusion_matrix, classification_report,
    roc_curve, roc_auc_score)

print(confusion_matrix(Ytest, y_pred))
#confusion matrix tell us what model classified each value
iris.target_names
#classified all correct setosa and virginica
#classified 1 wrong for versicolor 


print(classification_report(Ytest, y_pred, target_names=iris.target_names))
#precision:Out of all the times the model predicted a class, how many were actually correct?
#recall:Out of all the actual instances of a class, how many did the model correctly identify?

#model evaluation
x_train_pred = clf.predict(Xtrain)

y_pred = clf.predict(Xtest)
accuracy = accuracy_score(Ytest, y_pred)

accuracy
#test accuracy

accuracy1 = accuracy_score(Ytrain,x_train_pred)
#train accuracy


print(confusion_matrix(Ytrain, x_train_pred))

print(classification_report(Ytrain, x_train_pred, target_names=iris.target_names))
#precision:Out of all the times the model predicted a class, how many were actually correct?
#recall:Out of all the actual instances of a class, how many did the model correctly identify?

from sklearn.model_selection import cross_val_score

cross_validation=cross_val_score(clf,Xtrain,Ytrain,cv=5)
print(cross_validation)
print(cross_validation.mean())
#mean of cross fold validation accuracy

cross_validation.mean()

