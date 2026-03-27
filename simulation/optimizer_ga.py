import numpy as np

def run_ga():

    pop = np.random.rand(20,3)

    for _ in range(40):

        scores = pop.sum(axis=1)

        best = pop[np.argsort(scores)[-10:]]

        new = []

        while len(new) < 20:

            p1,p2 = best[np.random.randint(10)], best[np.random.randint(10)]

            child = (p1+p2)/2 + np.random.normal(0,0.05,3)

            child = np.clip(child,0,1)

            new.append(child)

        pop = np.array(new)

    return pop[0]