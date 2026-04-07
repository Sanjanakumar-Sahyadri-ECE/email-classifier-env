import random

class EmailEnv:
    def __init__(self):
        self.email = ""
        self.label = ""

        self.data = [
            ("Win money now!!!", "spam"),
            ("Meeting at 5 PM", "not spam"),
            ("Limited time offer", "spam"),
            ("Project submission tomorrow", "not spam"),
            ("Congratulations! You got a prize", "spam"),
            ("Team meeting rescheduled", "not spam")
        ]

    def reset(self):
        self.email, self.label = random.choice(self.data)
        return self.email

    def step(self, action):
        action = action.lower().strip()

        if action == self.label:
            reward = 1
            done = True
        elif action in ["spam", "not spam"]:
            reward = -0.5
            done = False
        else:
            reward = -1
            done = False

        return self.email, reward, done, {}

    def state(self):
        return self.email