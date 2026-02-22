import pandas as pd

data = pd.DataFrame(
{'Age': [20, 22, 19, None, 21, 23, None, 20],
'Study_Hours': [5, 3, 4, 2, None, 6, 4, 5],
'Gender': ['F', 'M', 'F', 'F', 'M', 'M', 'F', None],
'Department': ['IT', 'Business', 'IT', 'Arts', 'Business', 'IT', 'Arts', 'IT'],
'Final_Score': [75, 60, 70, 55, 65, 85, 58, 78]})

print(data)

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

numeric_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder())])

preprocessor = ColumnTransformer([
    ('num', numeric_pipeline, ['Age', 'Study_Hours']),
    ('cat', categorical_pipeline, ['Gender', 'Department'])
])

processed = preprocessor.fit_transform(data)
processed.shape

