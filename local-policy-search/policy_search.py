import random
import gymnasium as gym
import copy


def randomPolicy():
    policy = []
    for i in range(48):
        policy.append(random.randrange(0,4))
    return policy

def getRow(s):
    s1 = copy.deepcopy(s)
    row = s1//12
    return row

def getCol(s):
    s1 = copy.deepcopy(s)
    col = s1%12
    return col

def getDis(s):
    row = getRow(s)
    col = getCol(s)
    dis = abs(11-col)+abs(3-row)
    return dis

def HillClimb(policy): 
    bestDistance = 1000000000000
    bestPolicy = copy.deepcopy(policy)
    s = 36
    bestPosition = copy.deepcopy(s)
    while bestDistance > 0:
        if s == 36:
            if policy[s] == 1 or policy[s] == 2 or policy[s] == 3:
                print("bad starting policy")
                return []
        env = gym.make("CliffWalking-v0", render_mode = None)
        observation, info = env.reset()
        s = copy.deepcopy(observation)
        for i in range(25):
            observation, reward, terminated, truncated, info = env.step(bestPolicy[s])
            s = copy.deepcopy(observation)
            if OBJECTIVE(s) < bestDistance and s != 36:
                bestDistance = OBJECTIVE(s)
                bestPosition = copy.deepcopy(s)
                print(bestPosition, " new best position")
                print(bestDistance, " distance of new best position from goal")
        env.close()
        for n in NEIGHBORS(bestPosition, bestPolicy):
            env = gym.make("CliffWalking-v0", render_mode = None)
            observation, info = env.reset()
            s = copy.deepcopy(observation)
            for i in range(50):
                observation, reward, terminated, truncated, info = env.step(n[s])
                s = copy.deepcopy(observation)
                if OBJECTIVE(s) < bestDistance and s != 36:
                    #print(OBJECTIVE(s))
                    bestPolicy = copy.deepcopy(n)
                    bestDistance = OBJECTIVE(s)
                    bestPosition = copy.deepcopy(s)
                    print(bestPosition, " new best position")
                    print(bestDistance, " distance of new best position from goal")
    return bestPolicy

def OBJECTIVE(s):
    dis = getDis(s)
    return dis

def NEIGHBORS(s, p):
    n1 = copy.deepcopy(p)
    n2 = copy.deepcopy(p)
    n3 = copy.deepcopy(p)
    n4 = copy.deepcopy(p)
    n1[s] = 0
    n2[s] = 1
    n3[s] = 2
    n4[s] = 3
    if n1[s] != 0 or n2[s] != 1 or n3[s] != 2 or n4[s] != 3:
        print("ERROR: neighbor generation not working")
        return
    neighbor_list = [n1, n2, n3, n4]
    return neighbor_list

def main(): #let main handle random restarting
    total_reward = 0
    runner = True
    print("generating new random policy")
    policy = randomPolicy()
    p = HillClimb(policy)
    test = False
    while test == False:
        if p == []:
            print("generating new random policy")
            policy = randomPolicy()
            p = HillClimb(policy)
        else:
            test = True
    env = gym.make("CliffWalking-v0", render_mode = None)
    observation, info = env.reset()
    s = copy.deepcopy(observation)
    while s != 47:
        observation, reward, terminated, truncated, info = env.step(p[s])
        s = copy.deepcopy(observation)
        total_reward += reward
    print(total_reward)
    return p

#main()



