#Create a date range and random sales data
#pd.date_range()- It creates a sequence of dates automatically.
import pandas as pd
import numpy as np
dates=pd.date_range(start='2024-01-01', periods=7)

sales=pd.DataFrame({'Dates': dates,
                    'sales':[300,400,500,600,700,600,700]})

sales.set_index('Dates',inplace=True)

sales.loc['2024-01-02']
#You want	Use
#Row by position (0,1,2…)	iloc
#Row by label/date/name	loc

sales.iloc[0]

#Resample data to weekly/monthly aggregates
sales.resample('W').sum()

sales.resample('M').sum()

sales['7_day_avg'] = sales['sales'].rolling(window=7).mean()

sales

#Create a date range for 30 consecutive days starting from 2024-02-01.
test=pd.date_range(start='2024-02-01',periods=30)
test

#Create a sales column with random integers between 50 and 200 for each date.
sales = np.random.randint(50, 201, size=30)
sales

#Combine the dates and sales into a pandas DataFrame.
comb=pd.DataFrame({'Dates': test,'sales':sales,})

#Convert the date column to datetime type (if it’s not already).
comb['Dates']=pd.to_datetime(comb['Dates'])

#Set the date column as the DataFrame index.
comb.set_index('Dates',inplace=True)

#Resample the data to weekly total sales and store it in weekly_sales.

#Resample the data to weekly average sales and store it in weekly_avg.

#Resample the data to monthly total sales and store it in monthly_sales.

#Resample the data to monthly average sales and store it in monthly_avg.

comb.resample('W').sum()

comb.resample('W').mean()

comb.resample('M').sum()

#Resample the data to monthly average sales and store it in monthly_avg.
comb.resample('M').mean()