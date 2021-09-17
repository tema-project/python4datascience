import numpy as np


fileData = np.genfromtxt('recs.csv', delimiter=';')
# print(fileData)
v = np.random.sample(fileData.shape[1])
# print(v)
res = fileData * v
np.savetxt('result.csv', res, delimiter=';')
# print(res)
