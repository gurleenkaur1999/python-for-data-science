#Create a 5x3 matrix and add a 1D array of length 3 to each row
import numpy as np
import pandas as pd
matrix=np.random.randint(low=1, high=10, size=(5,3))
print(matrix)

newrow=[[5,3,4],[2,3,6]]

new=np.vstack([matrix,newrow])

#Compute pairwise distances between 10 points in 2D space (without loops)


#Implement a simple moving average on a time series (without loops)


a=pd.DataFrame({'age':[23,24,25,26,27,28]})
a.rolling(window=3).mean()