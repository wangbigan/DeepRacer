# 基于三个基本原则
# 1. 尽量在靠近中线的位置或者跟中线平行的状态前进
# 2. 尽可能走直线
# 3. 尽可能提高完成度
# 4. 在1/2/3基础上，尽可能提高车速

def reward_function(params):
    reward = 0.0

    # Read input parameters
    # track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    abs_steering = abs(params['steering_angle'])
    # steps = params['steps']

    if abs_steering == 0:  # 角度为零时，收益与赛车在中心线行驶收益一致，均为收益最大化
        reward += 1
    else:
        reward += 1 / (distance_from_center + 1)

    if params['all_wheels_on_track']:
        reward += params['progress']

    reward += (speed / 4)

    return float(reward)
