import time
from prometheus_client import start_http_server

from data_loader import load_data, fetch_data
from environment import step
from db import insert_log
from metrics import *

load_data()

data = fetch_data()

start_http_server(8000)

print("Simulation started...")

while True:
    for row in data:

        solar, wind, demand, _ = row

        gen, dem, bat, eff = step(solar, wind, demand)

        # Prometheus metrics
        energy_generation.set(gen)
        energy_demand.set(dem)
        battery_level.set(bat)
        efficiency_metric.set(eff)

        # Store in DB
        insert_log(gen, dem, bat, eff)

        print(f"{gen:.2f}, {dem:.2f}, {bat:.2f}, {eff:.2f}")

        time.sleep(2)