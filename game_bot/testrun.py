import gym
import requests

#Initialize the environment
env = gym.make('CartPole-v0')
env.reset()

for _ in range(1000):
    # Render the env
    env.render()
    
    # Randomly picks action on moving stick
    env.step(env.action_space.sample())
