# 基于三个基本原则
# 1. 尽可能与中线平行行驶
# 2. 尽可能靠近中线
# 3. 尽可能提高车速
# 4. 尽可能提高完成度


def reward_function(params):
    reward = 0.0

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed = params['speed']
    abs_steering = abs(params['steering_angle'])

    if distance_from_center < 0.6 * track_width:
        reward += 1 / (abs_steering / 100 + 1)  # 角度越小，奖励越高，角度为零和在中心线上行驶奖励同时最大化
        reward += 1 / (distance_from_center + 1)  # 越靠近中心，奖励越高
        reward += (speed / 2)  # 速度越快，奖励越高
        reward += (params['progress'] / 2)  # 完成度越高，奖励越高

    return float(reward)
