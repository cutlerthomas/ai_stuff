import gymnasium as gym
import random

big_total = 0
for i in range(500):
    env = gym.make("LunarLander-v2")

    observation, info = env.reset()

    x, y, xV, yV, a, aV, cL, cR = observation
    total_reward = 0
    action = 0
    counter = 0
    totalval = 0
    terminated = False
    truncated = False
    half_y = 0.7
    goal_r = 0.25
    goal_l = -0.25
    lean_r = -0.25
    lean_l = 0.25
    while not (terminated or truncated):
        x, y, xV, yV, a, aV, cL, cR = observation
        observation, reward, terminated, truncated, info = env.step(action)
        if cL == 1 or cR == 1:
            action = 0
        if a < -0.2:
            action = 1
        elif a > 0.2:
            action = 3
        elif yV < -1.3:
            action = 2
        elif x > goal_r:
            if a < -0.2:
                action = 3
            else:
                action = 2
        elif x < goal_l:
            if a > 0.2:
                action = 1
            else:
                action = 2
        total_reward += reward
    big_total += total_reward

    env.close()
big_total = big_total/500
print(big_total)
