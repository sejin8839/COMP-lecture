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
