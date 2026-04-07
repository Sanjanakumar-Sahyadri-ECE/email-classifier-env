from env import EmailEnv

env = EmailEnv()
state = env.reset()

print("Email:", state)

done = False
while not done:
    action = input("Enter prediction (spam/not spam): ")
    state, reward, done, _ = env.step(action)
    print("Reward:", reward)