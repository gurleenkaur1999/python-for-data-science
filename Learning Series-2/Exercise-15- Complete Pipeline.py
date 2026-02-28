import pandas as pd
from sklearn.linear_model import LogisticRegression

Titanic= pd.read_csv("C:/users/gurle/Downloads/Learning Series/Learning Series-2/Titanic-Dataset (1).csv")

print(Titanic)
Titanic.head()
Titanic.shape
#891 rows 12 cols

Titanic.isna().sum()
#Age,Cabin, embarked has missing values


Titanic.describe()
#numeric cols in the data 
#Passenger ID not a useful column to keep
#max age of passenger on this ship is 80
# max fare is 512 

Titanic['Survived'].value_counts()
#342 passengers survived
#549 passengers

Titanic['Survived'].value_counts(normalize=True)
#38% passengers survived
# 61% of passengers didn't survive
Titanic[['Pclass','Survived']].value_counts(normalize=True)
Titanic[['Pclass','Survived']].value_counts()

Titanic.groupby(['Pclass'])['Survived'].value_counts(normalize=True).unstack()
# highest survival rate on pclass 1
# medium survival on pclass2
#lowest survival on pclass 3
import matplotlib.pyplot as plt
Titanic['Age'].hist()
plt.show()

Titanic['Fare'].hist()
plt.show()


#Handles missing values and outliers

from sklearn.model_selection import train_test_split

X= Titanic.drop(['PassengerId','Name','Ticket','Cabin','Survived'],axis=1)
#dropping the variables not required
Y= Titanic['Survived']


x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=86)

#x_train has independend variables
#y_train has target variable
#x_test has independe varibables
#y_test has target variable

#Preprocesses features
#Trains multiple models
#Evaluates and selects best model
#Makes predictions on new data
#Visualizes results

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

numeric_pipeline = Pipeline([
    ('imputer',SimpleImputer(strategy='median')),
    ('scaling',StandardScaler())])


categorical_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot',OneHotEncoder(drop='first'))])

from sklearn.compose import ColumnTransformer

preprocessing = ColumnTransformer([
    ('numeric',numeric_pipeline,['Age','Fare']),
    ('categoric',categorical_pipeline,['Sex','Embarked'])
])

from sklearn.metrics import mean_squared_error, r2_score

from sklearn.neighbors import KNeighborsClassifier

Total_pipeline=Pipeline([('preprocessor',preprocessing),('model',LogisticRegression())
     ])

param_grid=[
    {'model': [LogisticRegression()]},
    {'model':[KNeighborsClassifier()],
     'model__n_neighbors': [2,3,5]}
     ]

#specifying models to predict target variable

grid= GridSearchCV(Total_pipeline,param_grid,cv=5)
grid.fit(x_train,y_train)
#apply transform automatically
grid.best_estimator_
#chose logistic regression
grid_pred=grid.best_estimator_.predict(x_test)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, grid_pred)
#correct predictions/total predictions
print("Accuracy:", accuracy)
#78% accuracy

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

cm = confusion_matrix(y_test, grid_pred)
cm
#False positive should be taken into consideration



