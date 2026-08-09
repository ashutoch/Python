import numpy as np


#! Handling Missing values 
#* In real-world datasets (excel, csv, database) we often gave some missing values (NaN). NumPy gives us tools to detect and handle them

data = np.array([10, 20, 30, np.nan, 70, np.nan, 10])   # nan = not a number

print(data)

#* Detecting missing values
print(np.isnan(data))

#* Removing missing values
print(data[~np.isnan(data)])

#* Counting missing values
print(np.isnan(data).sum())

#* Replacing missing values with mean value
# print(data[~np.isnan(data)].mean())
# data[np.isnan(data)] = data[~np.isnan(data)].mean()
# print(data)

mean = np.nanmean(data)
cleanData = np.where(np.isnan(data), mean, data)    # np.where(condition, if_true, if_false)
print(cleanData)
