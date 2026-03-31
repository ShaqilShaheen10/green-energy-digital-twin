import mysql.connector
import csv

def load_data():
    conn = mysql.connector.connect(
        host="mysql",
        user="root",
        password="root",
        database="energy"
    )
    cursor = conn.cursor()

    with open("/app/data/green_energy_dataset.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            cursor.execute("""
                INSERT INTO energy_data (solar, wind, demand, generation)
                VALUES (%s, %s, %s, %s)
            """, (
                float(row["solar"]),
                float(row["wind"]),
                float(row["demand"]),
                float(row["generation"])
            ))

    conn.commit()
    cursor.close()
    conn.close()


def fetch_data():
    conn = mysql.connector.connect(
        host="mysql",
        user="root",
        password="root",
        database="energy"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT solar, wind, demand, generation FROM energy_data")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data