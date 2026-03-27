import pandas as pd
from db import cursor, conn

def load_data():

    df = pd.read_csv("data/green_energy_dataset.csv")

    for _, row in df.iterrows():

        cursor.execute(
            "INSERT INTO dataset (energy_consumption,renewable_energy,carbon_emission) VALUES (%s,%s,%s)",
            (
                row["Energy_Consumption"],
                row["Renewable_Energy"],
                row["Carbon_Emission"]
            )
        )

    conn.commit()

    print("Dataset Loaded!")