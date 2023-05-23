import numpy as np

ls1 = [3,4,5,6]
s1=np.array(ls1)
ls2=[1,2,3,4]
s2=np.array(ls2)
c=ls1+ls2
d=s1+s2

print(c)
print(d)

import pandas as pd
Names = pd.Series(["Avery Bradley", "Jhon Hollan",
            "Jonas Jerebko", "Jordan Mickey",
            "Terry Rozer", "Jared Sullinger",])
print(Names)

import pandas as pd
data = {'Seoul': "South Korea", 'Tokyo':
"Japan","Sydney":"Australia"}
print(data)
countries= pd.Series(data )
print(countries)

import pandas as pd
df = pd.DataFrame({'Name': pd.Series(['Alice', 'Bob', 'Chris']),
'Age': pd.Series([21, 25, 23])})
print(df)
print(df.shape)
print(df.size)

import pandas as pd
df = pd.DataFrame( [['Jan',68,4.2,150,97.7,95.95],
['Feb',97,4.5,170,98,98.02],
['Mar',70,4.8,300,98.6,98.34],
['Apr',126,5.0,250,98.6,99.02],
['May',152,6.3,445,99,99.48],
['Jun',183,5.6,317,98.4,98.11],
['Jul',212,8.5,284,99.1,97.0],
['Aug',240,9.1,400,97.9,100],
['Sep',115,11.1,333,98,96.5],
['Oct',98,7.5,155,98.6,98.81],
['Nov',164,8.1,184,99.5,97.7],
['Dec',158,4.2,273,101.3,99.56]],
index=[0,1,2,3,4,5,6,7,8,9,10,11],
columns=['month','HbA1c mg/dl','WBC','plateletK/ml’,'temperature F’,’O2 %']

print(df.tail())