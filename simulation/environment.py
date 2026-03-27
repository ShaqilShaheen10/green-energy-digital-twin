import random

battery = 50

def step(solar, wind, grid):

    global battery

    demand = random.uniform(30,70)

    generation = solar + wind + grid

    surplus = generation - demand

    battery = max(0,min(100,battery + surplus*0.2))

    efficiency = generation/(demand+1)

    return generation, demand, battery, efficiency