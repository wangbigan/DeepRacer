# 基于三个基本原则
# 1. 代理距离赛道中线不能超过0.5个赛道宽度
# 2. 在1的前提下，保证速度最快
# 3. 在1和2的前提下，保证尽可能走直线

def reward_function(params):
    reward = 0.0

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    abs_steering = abs(params['steering_angle'])
    steps = params['steps']

    if distance_from_center > 0.55 * track_width:
        reward = -3 * steps  # 根据完成脚步数进行负向激励，保证出现该情况，返回值为负
    elif abs_steering == 0:  # 角度为零时，收益与赛车在中心线行驶收益一致，均为收益最大化
        reward = 2 * speed
    else:
        reward = 2 * speed / (distance_from_center + 1)

    return float(reward)