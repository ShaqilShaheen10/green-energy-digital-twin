import mysql.connector

conn = mysql.connector.connect(
    host="mysql",
    user="root",
    password="root",
    database="energy"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS energy_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    generation FLOAT,
    demand FLOAT,
    battery FLOAT,
    efficiency FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS dataset (
    id INT AUTO_INCREMENT PRIMARY KEY,
    energy_consumption FLOAT,
    renewable_energy FLOAT,
    carbon_emission FLOAT
)
""")

conn.commit()


def insert_log(gen, dem, bat, eff):
    cursor.execute(
        "INSERT INTO energy_logs (generation,demand,battery,efficiency) VALUES (%s,%s,%s,%s)",
        (gen, dem, bat, eff)
    )
    conn.commit()