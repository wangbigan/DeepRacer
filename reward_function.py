# 基于三个基本原则
# 1. 代理距离赛道中线不能超过0.5个赛道宽度
# 2. 在1的前提下，保证速度最快
# 3. 在1和2的前提下，保证尽可能走直线

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
