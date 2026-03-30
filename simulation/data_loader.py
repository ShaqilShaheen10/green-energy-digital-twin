import mysql.connector

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