import matplotlib.pyplot as plt
import matplotlib.patches as patches
from param import Parameter as p
import numpy as np
import env

########    
#経路を環境に表示する関数
########

def vis_path_env1(x, y):
    fig, ax = plt.subplots()
    
    #vectorをmatrixに変換
    ax.scatter(x, y, marker='x', color='red', s=5)
    
    env_data = env.Env1()
    wall_list = env_data.obs_boundary
    obstacle_list = env_data.obs_circle
    
    #wallを配置
    for k in range(len(wall_list)):
        wall = patches.Rectangle((wall_list[k][0], wall_list[k][1]), wall_list[k][2], wall_list[k][3], linewidth=1, edgecolor='black', facecolor='black')
        ax.add_patch(wall)
    
    #障害物を配置
    for k in range(len(obstacle_list)):
        x_o, y_o, r_o = obstacle_list[k][0], obstacle_list[k][1], obstacle_list[k][2],
        circle_obstacle = patches.Circle((x_o, y_o), radius=r_o, edgecolor='black', fill=False)
        ax.add_patch(circle_obstacle)
    
    #startとgoalを配置
    ax.scatter([x[0]], [y[0]], marker='v', color='green', label='start')
    ax.scatter([x[-1]], [y[-1]], marker='^', color='green', label='goal')
    
    ax.set_xlabel(r'$x$[m]')
    ax.set_ylabel(r'$y$[m]')
    ax.set_xlim([p.x_min - p.margin, p.x_max + p.margin])
    ax.set_ylim([p.y_min - p.margin, p.y_max + p.margin])
    
    ax.set_aspect('equal')
    ax.legend(loc="best")
    plt.show()
    
    return None

def vis_path_env2(x, y):
    fig, ax = plt.subplots()
    
    #vectorをmatrixに変換
    ax.scatter(x, y, marker='x', color='red', s=5)
    
    env_data = env.Env2()
    wall_list = env_data.obs_boundary
    obs_rectangle = env_data.obs_rectangle
    obs_circle = env_data.obs_circle
    
    #wallを配置
    for k in range(len(wall_list)):
        wall = patches.Rectangle((wall_list[k][0], wall_list[k][1]), wall_list[k][2], wall_list[k][3], linewidth=1, edgecolor='black', facecolor='black')
        ax.add_patch(wall)
    
    #障害物を配置
    for k in range(len(obs_rectangle)):
        x0, y0, w, h = obs_rectangle[k][0], obs_rectangle[k][1], obs_rectangle[k][2], obs_rectangle[k][3]
        rectangle_obstacle = patches.Rectangle((x0, y0), w, h, linewidth=1, edgecolor='black', facecolor='gray')
        ax.add_patch(rectangle_obstacle)
        
    for k in range(len(obs_circle)):
        x_o, y_o, r_o = obs_circle[k][0], obs_circle[k][1], obs_circle[k][2],
        circle_obstacle = patches.Circle((x_o, y_o), radius=r_o, edgecolor='black', facecolor='gray')
        ax.add_patch(circle_obstacle)
    
    #startとgoalを配置
    ax.scatter([x[0]], [y[0]], marker='v', color='green', label='start')
    ax.scatter([x[-1]], [y[-1]], marker='^', color='green', label='goal')
    
    ax.set_xlabel(r'$x$[m]')
    ax.set_ylabel(r'$y$[m]')
    ax.set_xlim([p.x_min - p.margin, p.x_max + p.margin])
    ax.set_ylim([p.y_min - p.margin, p.y_max + p.margin])
    
    ax.set_aspect('equal')
    ax.legend(loc="best")
    plt.show()
    
    return None

