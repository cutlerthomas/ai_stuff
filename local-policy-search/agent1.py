import gymnasium as gym
import policy_search



env = gym.make("CliffWalking-v0", render_mode = "human")
observation, info = env.reset()
policy = policy_search.main()
total_reward = 0
terminated = False
truncated = False
while not terminated or truncated:
        action = policy[observation]
        observation, reward, terminated, truncated, info = env.step(action)
env.close()
