import pandas as pd
#Load and display basic info (shape, dtypes, head, describe)
Iris=pd.read_csv('iris.csv')

#display basic info (shape, dtypes, head, describe)
Iris.shape

Iris.info()

#Check for missing values and duplicates
Iris.isna().sum()

Iris.describe()

Iris.duplicated().sum()


#Create a summary report: count of categorical values, distribution of numerical values
#Ask specific questions: "What's the survival rate by gender?" (Titanic) or "Average petal length by species?" (Iris)
Iris['species'].value_counts()

#Average petal length by species?" (Iris)
Iris.groupby('species')['petal_length'].mean()