from shopping_trip_env import ShoppingTripEnv
from itertools import permutations
import random
import math
import queue
import copy
import time


class Node:

    def __init__(self, l, p, a, d, g):
        
        self.location = l
        self.parent = p
        self.action = a
        self.depth = d
        self.goal = g


def ACTIONS(location, goal):
    actions = []
    if location[0] != 0:
        actions.append(3)
    if location[0] != 19:
        actions.append(1)
    if location[1] != 0:
        actions.append(0)
    if location[1] != 19:
        actions.append(2)
    if location == goal:
        actions.append(4)
    return actions

def RESULT(s, a):
    new_state = copy.deepcopy(s)
    if a == 0:
        if new_state.location[1] != 0:
            new_state.location = (new_state.location[0], new_state.location[1] - 1)
    elif a == 1:
        if new_state.location[0] != 19:
            new_state.location = (new_state.location[0] + 1, new_state.location[1])
    elif a == 2:
        if new_state.location[1] != 19:
            new_state.location = (new_state.location[0], new_state.location[1] + 1)
    elif a == 3:
        if new_state.location[0] != 0:
            new_state.location = (new_state.location[0] - 1, new_state.location[1])
    elif a == 4:
        if new_state.location == new_state.goal:
            new_state.goal = None
    return new_state

def GOAL_TEST(s):
    if s.num_items_left == 0 and s.agent_location == (0, 0):
        return True
    else:
        return False

def get_possible_paths(s):
    locations = []
    locations.append(s["apples"])
    locations.append(s["banana"])
    locations.append(s["yogurt"])
    locations.append(s["pizza"])
    locations.append(s["noodles"])
    locations.append(s["chicken"])
    locations.append(s["soda"])
    locations.append(s["candy"])
    locations.append(s["chips"])
    locations.append(s["cereal"])
    possible_paths = list(permutations(locations))
    return possible_paths

def find_best_path(paths):
    shortest_path_len = math.inf
    best_path = paths[0]
    for i in paths:
        j = 0
        distance = 0
        while j <= 8:
            if j == 0:
                distance += abs(0 - i[j][0]) + abs(0 - i[j][1])
            distance += abs(i[j][0] - i[j+1][0]) + abs(i[j][1] - i[j+1][1])
            if j == 8:
                distance += abs(i[j+1][0] - 0) + abs(i[j+1][1] - 0)
            j += 1
        if distance < shortest_path_len:
            best_path = i
            shortest_path_len = distance
    return best_path

def get_distance(start, end):
    distance = abs(start[0] - end[0]) + abs(start[1] - end[1])
    return distance

def bfs(s0):
    q = queue.Queue()
    q.put(s0)
    while q.empty() == False:
        s = q.get()
        if s.goal == None:
            return s
        for a in ACTIONS(s.location, s.goal):
            s1 = RESULT(s, a)
            if s1.goal == None or get_distance(s1.location, s1.goal) < get_distance(s.location, s.goal) or a == 4:
                s1.parent = s
                s1.depth = s.depth + 1
                s1.action = a
                q.put(s1)
    print("no path to goal found")

total_time = 0
max_reward = -math.inf
min_reward = math.inf
max_time = -math.inf
min_time = math.inf
avg_reward = 0
for i in range(100):
    start_time = time.time()
    env = ShoppingTripEnv()
    observation, info = env.reset()
    total_reward = 0
    possible_paths = get_possible_paths(observation)
    best_path = find_best_path(possible_paths)
    print(best_path)
    print(env.num_items_left)
    print(observation)
    i = 0
    while GOAL_TEST(env) == False:
        if i < 10:
            init_node = Node((observation["agent"]), None, None, 0, best_path[i])
            print(best_path[i])
        elif i == 10:
            init_node = Node((observation["agent"]), None, None, 0, (0, 0))
        goal = bfs(init_node)
        solution = []
        parent = goal.parent
        if i < 10:
            i += 1
        while parent.parent != None:
            solution.append(parent.action)
            new_parent = parent.parent
            parent = new_parent
        solution.append(4)
        while len(solution) > 0:
            action = solution.pop()
            observation, reward, terminated, truncated, info = env.step(action)
            print(observation)
            total_reward += reward
        print(env.num_items_left)
    print(total_reward)
    avg_reward += total_reward
    if total_reward > max_reward:
        max_reward = total_reward
    if total_reward < min_reward:
        min_reward = total_reward
    print("shopping complete! all items have been grabbed and we have exited the store!")


    env.close()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)
    if elapsed_time > max_time:
        max_time = elapsed_time
    if elapsed_time < min_time:
        min_time = elapsed_time
    total_time += elapsed_time
avg_reward = avg_reward//100
avg_time = total_time//100
print("average reward over 100 instances: ", avg_reward)
print("lowest reward over 100 instances: ", min_reward)
print("highest reward over 100 instances: ", max_reward)
print("average time over 100 instances: ", avg_time)
print("lowest time over 100 instances: ", min_time)
print("highest time over 100 instances: ", max_time)
