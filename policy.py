import gym
env = gym.make('CartPole-v0')

observation = env.reset()

for _ in range(1000):


    env.render()

    cart_pos, cart_vel, pole_ang, ang_vel = observation


    #policy

    if pole_ang>0 :
        #if angle >0 then leaning towards the right
        action =1
    else:
        action=0 #moving toward left

    observation, reward, done, info = env.step(action)
