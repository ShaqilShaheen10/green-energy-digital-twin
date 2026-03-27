from prometheus_client import Gauge

energy_generation = Gauge('energy_generation_kw','Generation')
energy_demand = Gauge('energy_demand_kw','Demand')
battery_level = Gauge('battery_level','Battery')
efficiency_metric = Gauge('efficiency','Efficiency')