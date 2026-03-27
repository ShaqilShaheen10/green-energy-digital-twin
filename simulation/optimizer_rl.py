import numpy as np
import random

Q = np.zeros((10,5))

def choose_action(state):

    if random.random() < 0.2:
        return random.randint(0,4)

    return np.argmax(Q[state])