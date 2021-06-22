import pandas as pd
import numpy as np
import operator
fd=pd.read_csv("testt.csv")
data=fd.drop(columns=['Timestamp','name']) # add felid to drop (all field other then quesn)
w=pd.concat([pd.get_dummies(data[col]) for col in data], axis=1, keys=data.columns)
di={}
i=0

for index,row in w.iterrows():
    l=[]
    d={}
    z=row.to_numpy()
    for index,row in w.iterrows():
        q=row.to_numpy()
        re=z* q
        s=re.sum()/4
        if s!=0 and s!=1:
            d[fd['name'][index]]=s   # change 'name' field u want to retrive(eg = 'email')
        #l.append(d)
    di[fd['name'][i]]=d    # here also 
    i+=1
ndi={}
for i in di:
    l=sorted(di[i].items(), key=operator.itemgetter(1),reverse=True)[:3]
    name=[]
    for j in l:
        name.append(j[0])
    ndi[i]=name
print(ndi)
