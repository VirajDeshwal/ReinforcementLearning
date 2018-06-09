import gym


#Create Environment

env = gym.make('CartPole-v0')


#Reset the environment to intial stage

env.reset()


#render the Environment

for _ in range(1000):


    env.render()

    env.step(env.action_space.sample())
