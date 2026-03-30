battery = 50

def step(solar, wind, demand):

    global battery

    generation = solar + wind

    surplus = generation - demand

    battery = max(0, min(100, battery + surplus * 0.2))

    efficiency = generation / (demand + 1)

    return generation, demand, battery, efficiency