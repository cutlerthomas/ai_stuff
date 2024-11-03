import numpy as np
import random

import gymnasium as gym
from gymnasium import spaces



class ShoppingTripEnv(gym.Env):
    metadata = {"render_modes": ["human"]}

    def __init__(self, render_mode=None):
        self.window_size = 512
        self.observation_space = spaces.Dict(
            {"agent": spaces.MultiDiscrete([20, 20]),
             "apples": spaces.MultiDiscrete([20, 20]),
             "banana": spaces.MultiDiscrete([20, 20]),
             "yogurt": spaces.MultiDiscrete([20, 20]),
             "pizza": spaces.MultiDiscrete([20, 20]),
             "noodles": spaces.MultiDiscrete([20, 20]),
             "chicken": spaces.MultiDiscrete([20, 20]),
             "soda": spaces.MultiDiscrete([20, 20]),
             "candy": spaces.MultiDiscrete([20, 20]),
             "chips": spaces.MultiDiscrete([20, 20]),
             "cereal": spaces.MultiDiscrete([20, 20]),
             }
        )
        self.action_space = spaces.Discrete(5)

    def get_obs(self):
        return {
            "agent": self.agent_location,
            "apples": self.apple_location,
            "banana": self.banana_location,
            "yogurt": self.yogurt_location,
            "pizza": self.pizza_location,
            "noodles": self.noodle_location,
            "chicken": self.chicken_location,
            "soda": self.soda_location,
            "candy": self.candy_location,
            "chips": self.chip_location,
            "cereal": self.cereal_location
        }
    
    def reset(self):
        locations = []
        self.agent_location = (0,0)
        locations.append(self.agent_location)
        self.apple_location = (random.randrange(0,20), random.randrange(0,20))
        for i in locations:
            while i == self.apple_location:
                self.apple_location = (random.randrange(0,20), random.randrange(0,20))
        locations.append(self.apple_location)
        self.banana_location = (random.randrange(0,20), random.randrange(0,20))
        for i in locations:
            while i == self.banana_location:
                self.banana_location = (random.randrange(0,20), random.randrange(0,20))
        locations.append(self.banana_location)
        self.yogurt_location = (random.randrange(0,20), random.randrange(0,20))
        for i in locations:
            while i == self.yogurt_location:
                self.yogurt_location = (random.randrange(0,20), random.randrange(0,20))
        locations.append(self.yogurt_location)
        self.pizza_location = (random.randrange(0,20), random.randrange(0,20))
        for i in locations:
            while i == self.pizza_location:
                self.pizza_location = (random.randrange(0,20), random.randrange(0,20))
        locations.append(self.pizza_location)
        self.noodle_location = (random.randrange(0,20), random.randrange(0,20))
        for i in locations:
            while i == self.noodle_location:
                self.noodle_location = (random.randrange(0,20), random.randrange(0,20))
        locations.append(self.noodle_location)
        self.chicken_location = (random.randrange(0,20), random.randrange(0,20))
        for i in locations:
            while i == self.chicken_location:
                self.chicken_location = (random.randrange(0,20), random.randrange(0,20))
        locations.append(self.chicken_location)
        self.soda_location = (random.randrange(0,20), random.randrange(0,20))
        for i in locations:
            while i == self.soda_location:
                self.soda_location = (random.randrange(0,20), random.randrange(0,20))
        locations.append(self.soda_location)
        self.candy_location = (random.randrange(0,20), random.randrange(0,20))
        for i in locations:
            while i == self.candy_location:
                self.candy_location = (random.randrange(0,20), random.randrange(0,20))
        locations.append(self.candy_location)
        self.chip_location = (random.randrange(0,20), random.randrange(0,20))
        for i in locations:
            while i == self.chip_location:
                self.chip_location = (random.randrange(0,20), random.randrange(0,20))
        locations.append(self.chip_location)
        self.cereal_location = (random.randrange(0,20), random.randrange(0,20))
        for i in locations:
            while i == self.cereal_location:
                self.cereal_location = (random.randrange(0,20), random.randrange(0,20))
        locations.append(self.cereal_location)
        self.num_items_left = 10
        
        observation = self.get_obs()
        info = None
        return observation, info
    
    def step(self, action):
        reward = 0
        if action == 0:
            if self.agent_location[1] != 0:
                self.agent_location = (self.agent_location[0], self.agent_location[1] - 1)
                reward = -1
            else:
                reward = -5
        elif action == 1:
            if self.agent_location[0] != 19:
                self.agent_location = (self.agent_location[0] + 1, self.agent_location[1])
                reward = -1
            else:
                reward = -5
        elif action == 2:
            if self.agent_location[1] != 19:
                self.agent_location = (self.agent_location[0], self.agent_location[1] + 1)
                reward = -1
            else:
                reward = -5
        elif action == 3:
            if self.agent_location[0] != 0:
                self.agent_location = (self.agent_location[0] - 1, self.agent_location[1])
                reward = -1
            else:
                reward = -5
        elif action == 4:
            if self.agent_location == self.apple_location:
                self.apple_location = (None, None)
                self.num_items_left -= 1
                reward = 5
            elif self.agent_location == self.banana_location:
                self.banana_location = (None, None)
                self.num_items_left -= 1
                reward = 5
            elif self.agent_location == self.yogurt_location:
                self.yogurt_location = (None, None)
                self.num_items_left -= 1
                reward = 5
            elif self.agent_location == self.pizza_location:
                self.pizza_location = (None, None)
                self.num_items_left -= 1
                reward = 5
            elif self.agent_location == self.noodle_location:
                self.noodle_location = (None, None)
                self.num_items_left -= 1
                reward = 5
            elif self.agent_location == self.chicken_location:
                self.chicken_location = (None, None)
                self.num_items_left -= 1
                reward = 5
            elif self.agent_location == self.soda_location:
                self.soda_location = (None, None)
                self.num_items_left -= 1
                reward = 5
            elif self.agent_location == self.candy_location:
                self.candy_location = (None, None)
                self.num_items_left -= 1
                reward = 5
            elif self.agent_location == self.chip_location:
                self.chip_location = (None, None)
                self.num_items_left -= 1
                reward = 5
            elif self.agent_location == self.cereal_location:
                self.cereal_location = (None, None)
                self.num_items_left -= 1
                reward = 5
            else:
                reward = -10
        if self.num_items_left == 0 and self.agent_location == (0, 0):
            terminated = True
            reward = 100
        else:
            terminated = False
        observation = self.get_obs()
        info = None
        #self.render()
        return observation, reward, terminated, False, info
    
    def render(self):
        grid = np.full((20,20), " ")
        grid[self.agent_location] = "A"
        grid[self.apple_location] = "a"
        grid[self.banana_location] = "b"
        grid[self.yogurt_location] = "y"
        grid[self.pizza_location] = "p"
        grid[self.noodle_location] = "n"
        grid[self.chicken_location] = "c"
        grid[self.soda_location] = "s"
        grid[self.candy_location] = "t"
        grid[self.chip_location] = "l"
        grid[self.cereal_location] = "m"
        print(f"{grid} \n")
    
    def close(self):
        pass

        