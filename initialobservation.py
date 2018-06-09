import gym

#CREATE Environment
env = gym.make('CartPole-v0')

print('INITIAL OBSERVATION')

#RESET THE STATE
observation = env.reset()
print(observation)

#RENDER THE STATE
for _ in range(2):
    action = env.action_space.sample()
    observation,reward,done, info = env.step(action)
    print('\n')

    print("Performed One Random Action")
    print('\n')
    print(observation)
    print('\n')

    print('reward')
    print(reward)
    print('\n')

    print('Done')
    print(done)
    print('\n')

    print('Info')
    print(info)
    print('\n')
