#!/usr/bin/env python3

from pettingzoo.classic import connect_four_v3
import connect_four_model
import time
import copy
import random
import best_agent
#import agent1
#import agent2
import random_agent

def main():
    player0wins = 0
    player1wins = 0
    for i in range (1):
        agent_function = { "player_0": random_agent.agent_function, "player_1": best_agent.agent_function }
        #agent_function = { "player_0": random_agent.agent_function, "player_1": random_agent.agent_function }
        times = { "player_0": 0.0, "player_1": 0.0 }

        env = connect_four_v3.env(render_mode="human")
        #env = connect_four_v3.env(render_mode=None)
        env.reset()

        for agent in env.agent_iter():
            if True:
                """text display of board"""
                env1 = connect_four_model.ConnectFour()
                env1.copy_from_env(env)
                print(env1)
                print()
                print()
                print()
            t1 = time.time()
            if agent == "player_0":
                action = int(input("please enter a column to place your piece. Columns range from 0-6"))
            else:
                action = agent_function[agent](env, agent)
            t2 = time.time()
            times[agent] += (t2-t1)

            env.step(action)
            try:
                observation, reward, termination, truncation, info = env.last()
                print("{} took action {}".format(agent, action))
                if termination or truncation:
                    if len(env.rewards.keys()) == 2:
                        winner = None
                        for a in env.rewards:
                            if env.rewards[a] == 1:
                                winner = a
                                break
                        if winner is not None:
                            print(f"{winner} wins.")
                            if winner == "player_1":
                                player1wins += 1
                            elif winner == "player_0":
                                player0wins += 1
                        else:
                            print("Not sure who won.")
                        if True:
                            """text display of board"""
                            env1 = connect_four_model.ConnectFour()
                            env1.copy_from_env(env)
                            print(env1)
                            print()
                            print()
                            print()
                        break
            except:
                pass

        time.sleep(10) # useful for end of game with human render mode
        env.close()

        for agent in times:
            print(f"{agent} took {times[agent]:8.5f} seconds.")
    #print("player_0 wins", player0wins)
    #print("player_1 wins", player1wins)
    return

if __name__ == "__main__":
    if False:
        import cProfile
        cProfile.run('main()')
    else:
        main()