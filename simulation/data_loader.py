import pandas as pd
import mysql.connector

def load_data():
    df = pd.read_csv("data/green_energy_dataset.csv")

    conn = mysql.connector.connect(
        host="mysql",
        user="root",
        password="root",
        database="energy"
    )

    cursor = conn.cursor()

    # Create table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS energy_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        solar FLOAT,
        wind FLOAT,
        demand FLOAT,
        generation FLOAT
    )
    """)

    # Insert data
    for _, row in df.iterrows():
        cursor.execute("""
        INSERT INTO energy_data (solar, wind, demand, generation)
        VALUES (%s, %s, %s, %s)
        """, (
            float(row[0]),
            float(row[1]),
            float(row[2]),
            float(row[3])
        ))

    conn.commit()
    cursor.close()
    conn.close()

    print("Dataset loaded into MySQL")