import numpy as np
import pandas as pd
qqq=pd.Series([1,2,3])
print(qqq)
s1 = pd.Series([1,2,3])
s2 = pd.Series([4,5,6])
s3 = pd.Series([7,8,9], index=['a','b','c'])
s4 = pd.Series([10,11,12], index=['d','e','f'])
print(s1)
print(s2)
print(s3)
print(s4)