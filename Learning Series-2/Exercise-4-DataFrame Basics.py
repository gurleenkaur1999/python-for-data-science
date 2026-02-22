#Create a DataFrame with student data (name, age, scores in 3 subjects)


#Sort by multiple columns


import pandas as pd

Data_Students=pd.DataFrame([{'name':'Gurleen','Age': 26, 'math':40,'stat': 90,'phys':78},
                           {'name':'Prah','Age': 29, 'math':40,'sst': 43,'phys':68}])
  #Handle missing values: detect, fill with mean/median, drop rows                         
Data_Students=Data_Students.fillna(0)

#Add new columns (total score, average, grade based on average)

Data_Students['total']=Data_Students['math']+Data_Students['stat']+Data_Students['phys']+Data_Students['sst']

Data_Students['Average']=Data_Students[['math','stat','phys','sst']].mean(axis=1)

#Filter students who scored above 80 in any subject
Data_Students[(Data_Students['math']>80) | (Data_Students['stat']>80)|(Data_Students['phys']>80)|(Data_Students['sst']>80)]

#Sort by multiple columns
Data_Students.sort_values(by='Average')

Data_Students.drop(0)

