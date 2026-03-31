import mysql.connector

conn = mysql.connector.connect(
    host="mysql",   
    user="root",
    password="root",
    database="energy"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS energy_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    solar FLOAT,
    wind FLOAT,
    demand FLOAT,
    generation FLOAT
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