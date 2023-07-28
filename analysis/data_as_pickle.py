import scipy.io  #  mat file read 
import pandas as pd
import numpy as np

import os
if not 'dataset_pkl' in os.listdir(): 
   os.mkdir('dataset_pkl')

def to_sec(vec):
    mon, day, hr, min, sec = vec[0][1:]
    return (mon*30*86400 + day*86400 + hr*3600 + min*60 + sec)

def save(mat):
    path = '../dataset/' 
    data = scipy.io.loadmat(path + mat)
    df = pd.DataFrame(data[mat[:-4]]['cycle'][0][0][0])  
    if mat_data['type'][0] == 'impedance':
        continue
    else:
        names = df['data'].dtype.names
        print(names)
    times_fromzero = [np.array(df['time'])[i] - np.array(df['time'][0]) for i in range(len(df))]
    times = []
   #  print(times_fromzero)
    for i in times_fromzero:
        times.append(to_sec(i))
    df['time'] = times
    df['data'] = np.array([[df['data'][i][0][0]] for i in range(len(df))])
    df.to_pickle('dataset_pkl/' + mat[:-4] + '.pkl')

names = ['B0005.mat','B0006.mat','B0007.mat','B0018.mat']
for i in names: 
    save(i)