import gymnasium as gym
import random
import queue
   

total_reward = 0

def main():
    totalReward = 0
    passSolution = []
    destSolution = []
    inCar = False
    goal = bfs(initRow, initCol, 1)
    newStartState = goal.state
    newRow = newStartState.row
    newCol = newStartState.col
    passSolution.append(goal.action)
    parent = goal.parent
    if parent == None:
        print("car started at passenger location")
    else:
        while parent.parent != None:
            passSolution.append(parent.action)
            newParrent = parent.parent
            parent = newParrent
        while len(passSolution) > 0:
            action = passSolution.pop()
            observation, reward, terminated, truncated, info = env.step(action)
            totalReward += reward
    action = 4
    observation, reward, terminated, truncated, info = env.step(action)
    totalReward += reward
    inCar = True
    goal = bfs(newRow, newCol, 2)
    destSolution.append(goal.action)
    parent = goal.parent
    while parent.parent != None:
        destSolution.append(parent.action)
        newParrent = parent.parent
        parent = newParrent
    while len(destSolution) > 0:
        action = destSolution.pop()
        observation, reward, terminated, truncated, info = env.step(action)
        totalReward += reward
    action = 5
    observation, reward, terminated, truncated, info = env.step(action)
    totalReward += reward
    env.close()
    return totalReward

def ACTIONS(s):
    actions = []
    if s.col == 0:
        if s.row == 0:
            actions = [0,2,4,5]
        elif s.row == 1 or 2:
            actions = [0,1,2]
        elif s.row == 3:
            actions = [0,1]
        elif s.row == 4:
            actions = [1,4,5]
    elif s.col == 1:
        if s.row == 0:
            actions = [0,3]
        elif s.row == 1:
            actions = [0,1,3]
        elif s.row == 2:
            actions = [0,1,2,3]
        elif s.row == 3:
            actions = [0,1,2]
        elif s.row == 4:
            actions = [1,2]
    elif s.col == 2:
        if s.row == 0:
            actions = [0,2]
        elif s.row == 1:
            actions = [0,1,2]
        elif s.row == 2:
            actions = [0,1,2,3]
        elif s.row == 3:
            actions = [0,1,3]
        elif s.row == 4:
            actions = [1,3]
    elif s.col == 3:
        if s.row == 0:
            actions = [0,2,3]
        elif s.row == 1 or 2:
            actions = [0,1,2,3]
        elif s.row == 3:
            actions = [0,1,2]
        elif s.row == 4:
            actions = [1,2,4,5]
    elif s.col == 4:
        if s.row == 0:
            actions = [0,3,4,5]
        elif s.row == 1 or 2 or 3:
            actions = [0,1,3]
        elif s.row == 4:
            actions = [1,3]
    return actions

def GOALTEST(s, count):
    if count == 2:
        if destination == 0:
            if s.row == 0 and s.col == 0:
                return True
            else:
                return False
        elif destination == 1:
            if s.row == 0 and s.col == 4:
                return True
            else:
                return False
        elif destination == 2:
            if s.row == 4 and s.col == 0:
                return True
            else:
                return False
        elif destination == 3:
            if s.row == 4 and s.col == 3:
                return True
            else:
                return False
    elif passLoc == 0:
        if s.row == 0 and s.col == 0:
            return True
        else:
            return False
    elif passLoc == 1:
        if s.row == 0 and s.col == 4:
            return True
        else:
            return False
    elif passLoc == 2:
        if s.row == 4 and s.col == 0:
            return True
        else:
            return False
    elif passLoc == 3:
        if s.row == 4 and s.col == 3:
            return True
        else:
            return False
    elif passLoc == 4:
        GOALTEST(s, 2)
            
def RESULT(s,a):
    newcol = s.col
    newrow = s.row
    if a == 0:
        newrow = s.row + 1
    elif a == 1:
        newrow = s.row - 1
    elif a == 2:
        newcol = s.col + 1
    elif a == 3:
        newcol = s.col - 1
    elif a == 4 or 5:
        return s
    newState = State(newrow, newcol)
    return newState
    
class State:
    def __init__(self, curRow, column):
        self.row = curRow
        self.col = column
class Node:
    def __init__(self, s, p, a, d):
        self.state = s
        self.parent = p
        self.action = a
        self.depth = d

def bfs(row, col, count):
    d = 0
    initState = State(row, col)
    initNode = Node(initState, None, None, 0)
    q = queue.Queue()
    q.put(initNode)
    while q.qsize() > 0:
        d += 1
        n = q.get()
        s = n.state
        if GOALTEST(s, count):
            return n
        actions = ACTIONS(s)
        for a in actions:
            s1 = RESULT(s,a)
            n1 = Node(s1, n, a, d)
            q.put(n1)
    print("no goal found")

for i in range(1):
    env = gym.make("Taxi-v3", render_mode="human")
    observation, info = env.reset()
    initRow = ((observation//4)//5)//5
    initCol = ((observation//4)//5)%5
    passLoc = (observation//4) % 5
    destination = observation % 4
    rew = main()
    total_reward += rew

print(total_reward/1000)
