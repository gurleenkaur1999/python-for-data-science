import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    'Hours_Studied': [2, 4, 3, 5, None, 6, 1, 4],
    'Sleep_Hours': [7, 6, 8, 5, 6, None, 7, 5],
    'Gender': ['M', 'F', 'F', 'M', 'F', 'M', 'M', 'F'],
    'Course': ['Math', 'Science', 'Math', 'History', 'Science', 'Math', 'History', 'Math'],
    'Exam_Score': [50, 65, 60, 70, 68, 80, 45, 62]
})

print(data)
data.head()
data.shape

data.isna().sum()
#total 2 missing values


data.describe()
data.info()

#Handles missing values and outliers

from sklearn.model_selection import train_test_split

X= data.drop('Exam_Score',axis=1)
Y= data['Exam_Score']



x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2)

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
    ('imputer',SimpleImputer(strategy='mean')),
    ('scaling',StandardScaler())])


categorical_pipeline = Pipeline([
('imputer',SimpleImputer(strategy='most_frequent')),
    ('onehot',OneHotEncoder())])

from sklearn.compose import ColumnTransformer

preprocessing = ColumnTransformer([
    ('numeric',numeric_pipeline,['Hours_Studied','Sleep_Hours']),
    ('categoric',categorical_pipeline,['Gender','Course'])
])
X
transformed_x= preprocessing.fit_transform(x_train)

linmodel=LinearRegression()

linmodel.fit(transformed_x,y_train)

linmodel.coef_

transformed_x_test=preprocessing.transform(x_test)

y_pred=linmodel.predict(transformed_x_test)
y_pred

#second way


Total_pipeline=Pipeline([('preprocessor',preprocessing),('model',LinearRegression())
     ])

model=Total_pipeline.fit(x_train,y_train)
#fit here will learn the paramteres and applies the steps on xtraining data and goive it to the model

model.predict(x_test)
