import env, plot
import numpy as np

x_data = np.loadtxt('../data/env1/x.csv', delimiter=',',encoding="utf-8-sig")
y_data = np.loadtxt('../data/env1/y.csv', delimiter=',',encoding="utf-8-sig")
theta_data = np.loadtxt('../data/env1/theta.csv', delimiter=',',encoding="utf-8-sig")

sample_index = [0, 64, 6432, 12335]
    

x = x_data[sample_index]
y = y_data[sample_index]

#visual path of sample index
plot.vis_some_path_env1(x, y)
    