#Load a dataset of random numbers (1000 samples)
import numpy as np
data=np.random.randint(low=1, high=10, size=1000)
data
#Calculate mean, median, std, min, max along different axes
data.mean()
data.max()
data.min()
np.median(data)
#calculating mean and median on different axes
array_data=data.reshape((100,10))
array_data
array_data.mean(axis=0)
#column wise mean
#10 columns 10 mean values
array_data.mean(axis=1)
#100 means values
#Find percentiles (25th, 50th, 75th)
#np.percentile(array, percentile_value)
np.percentile(data,25)
np.percentile(data,75)
q1=np.percentile(data,25)
q3=np.percentile(data,75)
iqr=q3-q1
lowerbound=q1-1.5*iqr
lowerbound
upperbound=q3+1.5*iqr
upperbound
#normalizing the data
data_min=data.min()
data_max=data.max()
norm=(data-data_min)/(data_max-data_min)
norm
#normalization bringgs the data on same scale
#to exmplify if in data you have fare and age, fare will have higher values and age value will be between 1 and 100.. so we will bring data to same scale using n
#normalization technique. with that it will be comparable
