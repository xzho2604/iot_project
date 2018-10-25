from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C
import numpy as np
from sklearn.datasets import make_friedman2



def read_file():
    raw = []
    cordinate = []
    with open('../data02/clean_record.txt') as f:

        for line in f.readlines():
            line_data = line.strip('\n').split(',')
            raw.append([int(i) for i in line_data[:5]])
            cordinate.append([int(i) for i in line_data[5:7]])
    
    return raw, cordinate
raw_data, raw_label = read_file()
X = np.array(raw_data)
y = np.array(raw_label)

kernel = C(0.1, (0.001,0.1))*RBF(0.5,(1e-4,10))
reg = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10, alpha=0.1)
reg.fit(X, y)

print()
