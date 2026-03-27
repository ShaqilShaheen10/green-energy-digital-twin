import time
import random
import numpy as np

from prometheus_client import start_http_server

from environment import step
from optimizer_ga import run_ga
from db import insert_log
from metrics import *

from data_loader import load_data

# Load dataset
load_data()

start_http_server(8000)

best = run_ga()

print("Best config:", best)

while True:

    solar = best[0]*random.uniform(40,80)
    wind = best[1]*random.uniform(20,60)
    grid = best[2]*random.uniform(10,30)

    gen, dem, bat, eff = step(solar, wind, grid)

    energy_generation.set(gen)
    energy_demand.set(dem)
    battery_level.set(bat)
    efficiency_metric.set(eff)

    insert_log(gen, dem, bat, eff)

    print(f"{gen:.2f}, {dem:.2f}, {bat:.2f}, {eff:.2f}")

    time.sleep(5)