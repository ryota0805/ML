import plot
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def main_env1():
    x_data = np.loadtxt('../data/env1/first_quantile/first_quantile_x.csv', delimiter=',',encoding="utf-8-sig")
    y_data = np.loadtxt('../data/env1/first_quantile/first_quantile_y.csv', delimiter=',',encoding="utf-8-sig")
    theta_data = np.loadtxt('../data/env1/first_quantile/first_quantile_theta.csv', delimiter=',',encoding="utf-8-sig")
    
    vis_flag = [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]
    #vis_flag = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False]
    
    plot.vis_all_path_env1(x_data, y_data, theta_data, vis_flag)

def main_env2():
    x_data = np.loadtxt('../data/env2/x.csv', delimiter=',',encoding="utf-8-sig")
    y_data = np.loadtxt('../data/env2/y.csv', delimiter=',',encoding="utf-8-sig")
    theta_data = np.loadtxt('../data/env2/theta.csv', delimiter=',',encoding="utf-8-sig")
    
    plot.vis_all_path_env2(x_data[:1000, :], y_data, theta_data)
    
main_env1()
#main_env2()
