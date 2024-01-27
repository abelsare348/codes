#The Pandas Series can be defined as a one-dimensional array that is capable of storing various data types.
# like object but it has bydefault index with it. even we can give index as per our need.

import pandas as pd
import numpy as np
# info=['p','a','n','d','a','s']
# a=pd.Series()
# print(a)

data=[11.2,11.2,2]
b=pd.Series(data,[1,2,3])
print(b.index)
print(b.value_counts)  #return a series with unique values

c=b.copy
print("******\n",c)

d=pd.Series(list(['Aniket',np.nan]))
print(d.hasnans)