import env, plot
import numpy as np

x_data = np.loadtxt('../data/env1/x.csv', delimiter=',',encoding="utf-8-sig")
y_data = np.loadtxt('../data/env1/y.csv', delimiter=',',encoding="utf-8-sig")
theta_data = np.loadtxt('../data/env1/theta.csv', delimiter=',',encoding="utf-8-sig")

#よくない例：6000, 213,234,23
#よい例：567,1563
sample_index = 6000

if sample_index >= len(x_data):
    print("Over sample index")
    
else:
    x = x_data[sample_index]
    y = y_data[sample_index]
    theta_start = theta_data[sample_index][0]
    theta_goal = theta_data[sample_index][-1]
    
    #visual path of sample index
    print("初期姿勢：{}°, 終端姿勢：{}°".format(int(np.degrees(theta_start)), int(np.degrees(theta_goal))))
    plot.vis_path_env1(x, y)
    