from statistics import quantiles
import pandas as pd
import numpy as np

data = [4, 6, 6, 7, 8, 12, 15, 17, 20, 21, 21, 23, 24, 27, 28]
#Print o valor exato
[print(round(q, 1)) for q in quantiles(data, n=4)]
#printa valores excludentes ou a partir de %
data  = pd.Series(data)
print(data.describe())

print("Q2 quantile of arr : ", np.quantile(data, .50))
print("Q1 quantile of arr : ", np.quantile(data, .25))
print("Q3 quantile of arr : ", np.quantile(data, .75))