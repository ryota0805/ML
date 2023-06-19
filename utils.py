import env

#pathがcollision freeかどうか検証する関数
def is_collision_free(x, y):
    #set environment data
    env_data = env.Env1
    
    obs_circle = env_data.obs_circle()
    obs_rectangle = env_data.obs_rectangle()
    
    length = len(x)
    
    flag = True
    
    #各way pointに対して障害物外にあるかどうか確かめる
    for i in range(length):
        
        #長方形との衝突チェック
        for j in range(len(obs_rectangle)):
            xo, yo, w, h = obs_rectangle[j][0], obs_rectangle[j][1],obs_rectangle[j][2],obs_rectangle[j][3]
            x_min, x_max, y_min, y_max = xo, xo+w, yo, yo+h
            
            if x_min <= x[i] <= x_max and y_min <= y[i] <= y_max:
                flag = False
                break
            else:
                pass
            
        #円との衝突チェック
        for k in range(len(obs_circle)):
            xk, yk, rk = obs_circle[k][0], obs_circle[k][1], obs_circle[k][2]
            
            if (x[i] - xk) ** 2 + (y[i] - yk) ** 2 <= (rk - 0.5) ** 2:
                flag = False
                break
            else:
                pass
            
        if flag == False:
            break
        else:
            continue
    
    return flag



        
            
        