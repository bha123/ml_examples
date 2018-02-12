import gym

env = gym.make('CartPole-v0')

for i_episode in range(20):
    
    # Array of velocities
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        
        action = env.action_space.sample()
        # Reinforcement learning 
        observation, reward, done, info = env.step(action)
        if done:
            print("episode finished after {0} times".format(t))
            break  
