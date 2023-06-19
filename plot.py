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
    obs_rectangle = env_data.obs_rectangle
    obs_circle = env_data.obs_circle
    
    #wallを配置
    for k in range(len(wall_list)):
        wall = patches.Rectangle((wall_list[k][0], wall_list[k][1]), wall_list[k][2], wall_list[k][3], linewidth=1, edgecolor='black', facecolor='black')
        ax.add_patch(wall)
    
    #障害物を配置
    for k in range(len(obs_circle)):
        x_o, y_o, r_o = obs_circle[k][0], obs_circle[k][1], obs_circle[k][2],
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


def vis_some_path_env1(x, y):
    fig, ax = plt.subplots()
    colorlist = ["r", "y", "b", "c"]
    for i in range(np.shape(x)[0]):
        ax.scatter(x[i], y[i], marker='x', color=colorlist[i], s=5)
        #startとgoalを配置
        ax.scatter([x[i][0]], [y[i][0]], marker='v', color='green', label='start')
        ax.scatter([x[i][-1]], [y[i][-1]], marker='^', color='green', label='goal')
        
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
    
    ax.set_xlabel(r'$x$[m]')
    ax.set_ylabel(r'$y$[m]')
    ax.set_xlim([p.x_min - p.margin, p.x_max + p.margin])
    ax.set_ylim([p.y_min - p.margin, p.y_max + p.margin])
    
    ax.set_aspect('equal')
    #ax.legend(loc="best")
    plt.show()
    
    return None


#vis_all_path用
def vis_all_path_env1(x_data, y_data, theta_data, vis_flag):
    fig, ax = plt.subplots()
    
    env_data = env.Env1()
    wall_list = env_data.obs_boundary
    obstacle_list = env_data.obs_circle
    
    color_list = [(0, 0, 0, 0.5), 
                  (0.5, 0, 0, 0.5), 
                  (1, 0, 0, 0.5), 
                  (0, 0.5, 0, 0.5), 
                  (0, 1, 0, 0.5), 
                  (0, 0, 0.5, 0.5), 
                  (0, 0, 1, 0.5), 
                  (0.5, 0.5, 0, 0.5), 
                  (1, 0.5, 0, 0.5), 
                  (0.5, 1, 0, 0.5), 
                  (0, 0.5, 0.5, 0.5), 
                  (0, 1, 0.5, 0.5), 
                  (0, 0.5, 1, 0.5), 
                  (0.5, 0, 0.5, 0.5), 
                  (1, 0, 0.5, 0.5), 
                  (0.5, 0, 1, 0.5)]
    
    #thetaに対してpathを分類し、色違いで表示させる
    for i in range(np.shape(x_data)[0]):
        initial_theta, terminal_theta = theta_data[i][0], theta_data[i][-1]
        x, y = x_data[i], y_data[i]
        
        if -np.pi/2 <= initial_theta < -np.pi/4:
            if -np.pi/2 <= terminal_theta < -np.pi/4 and vis_flag[0]:
                ax.scatter(x, y, marker='x', color=color_list[0], s=5)
            elif -np.pi/4 <= terminal_theta < 0 and vis_flag[1]:
                ax.scatter(x, y, marker='x', color=color_list[1], s=5)
            elif 0 <= terminal_theta < np.pi/4 and vis_flag[2]:
                ax.scatter(x, y, marker='x', color=color_list[2], s=5)
            elif np.pi/4 <= terminal_theta < np.pi/2 and vis_flag[3]:
                ax.scatter(x, y, marker='x', color=color_list[3], s=5)
            else:
                pass
    
        elif -np.pi/4 <= initial_theta < 0:
            if -np.pi/2 <= terminal_theta < -np.pi/4 and vis_flag[4]:
                ax.scatter(x, y, marker='x', color=color_list[4], s=5)
            elif -np.pi/4 <= terminal_theta < 0 and vis_flag[5]:
                ax.scatter(x, y, marker='x', color=color_list[5], s=5)
            elif 0 <= terminal_theta < np.pi/4 and vis_flag[6]:
                ax.scatter(x, y, marker='x', color=color_list[6], s=5)
            elif np.pi/4 <= terminal_theta < np.pi/2 and vis_flag[7]:
                ax.scatter(x, y, marker='x', color=color_list[7], s=5)
            else:
                pass
            
        elif 0 <= initial_theta < np.pi/4:
            if -np.pi/2 <= terminal_theta < -np.pi/4 and vis_flag[8]:
                ax.scatter(x, y, marker='x', color=color_list[8], s=5)
            elif -np.pi/4 <= terminal_theta < 0 and vis_flag[9]:
                ax.scatter(x, y, marker='x', color=color_list[9], s=5)
            elif 0 <= terminal_theta < np.pi/4 and vis_flag[10]:
                ax.scatter(x, y, marker='x', color=color_list[10], s=5)
            elif np.pi/4 <= terminal_theta < np.pi/2 and vis_flag[11]:
                ax.scatter(x, y, marker='x', color=color_list[11], s=5)
            else:
                pass
                
        elif np.pi/4 <= initial_theta < np.pi/2:
            if -np.pi/2 <= terminal_theta < -np.pi/4 and vis_flag[12]:
                ax.scatter(x, y, marker='x', color=color_list[12], s=5)
            elif -np.pi/4 <= terminal_theta < 0 and vis_flag[13]:
                ax.scatter(x, y, marker='x', color=color_list[13], s=5)
            elif 0 <= terminal_theta < np.pi/4 and vis_flag[14]:
                ax.scatter(x, y, marker='x', color=color_list[14], s=5)
            elif np.pi/4 <= terminal_theta < np.pi/2 and vis_flag[15]:
                ax.scatter(x, y, marker='x', color=color_list[15], s=5)
            else:
                pass
        
    
    #wallを配置
    for k in range(len(wall_list)):
        wall = patches.Rectangle((wall_list[k][0], wall_list[k][1]), wall_list[k][2], wall_list[k][3], linewidth=1, edgecolor='black', facecolor='black')
        ax.add_patch(wall)
    
    #障害物を配置
    for k in range(len(obstacle_list)):
        x_o, y_o, r_o = obstacle_list[k][0], obstacle_list[k][1], obstacle_list[k][2],
        circle_obstacle = patches.Circle((x_o, y_o), radius=r_o, edgecolor='black', fill=False)
        ax.add_patch(circle_obstacle)
    
    
    ax.set_xlabel(r'$x$[m]')
    ax.set_ylabel(r'$y$[m]')
    ax.set_xlim([p.x_min - p.margin, p.x_max + p.margin])
    ax.set_ylim([p.y_min - p.margin, p.y_max + p.margin])
    
    ax.set_aspect('equal')
    ax.legend(loc="best")
    
    plt.show()
    

#vis_all_path用
def vis_all_path_env2(x_data, y_data, theta_data):
    fig, ax = plt.subplots()
    
    env_data = env.Env2()
    wall_list = env_data.obs_boundary
    obs_rectangle = env_data.obs_rectangle
    obs_circle = env_data.obs_circle
    
    #thetaに対してpathを分類し、色違いで表示させる
    for i in range(np.shape(x_data)[0]):
        initial_theta, terminal_theta = theta_data[i][0], theta_data[i][-1]
        x, y = x_data[i], y_data[i]
        
        ax.scatter(x, y, marker='x', color="r", s=5)
        
    
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
    
    
    ax.set_xlabel(r'$x$[m]')
    ax.set_ylabel(r'$y$[m]')
    ax.set_xlim([p.x_min - p.margin, p.x_max + p.margin])
    ax.set_ylim([p.y_min - p.margin, p.y_max + p.margin])
    
    ax.set_aspect('equal')
    ax.legend(loc="best")
    
    plt.show()