import sqlite3


# Create Database and Table
def create_database():

    conn = sqlite3.connect("devices.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS devices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        device_id TEXT,
        capability INTEGER,
        feature INTEGER,
        activity INTEGER,
        trust_score REAL,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()


# Insert Device
def insert_device(device_id, capability, feature, activity, trust_score, status):

    conn = sqlite3.connect("devices.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO devices
    (device_id, capability, feature, activity, trust_score, status)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (device_id, capability, feature, activity, trust_score, status))

    conn.commit()
    conn.close()


# View All Devices
def get_all_devices():

    conn = sqlite3.connect("devices.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM devices")

    rows = cursor.fetchall()

    conn.close()

    return rows


# Search Device
def search_device(device_id):

    conn = sqlite3.connect("devices.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM devices WHERE device_id=?",
        (device_id,)
    )

    row = cursor.fetchall()

    conn.close()

    return row


# Delete Device
def delete_device(device_id):

    conn = sqlite3.connect("devices.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM devices WHERE device_id=?",
        (device_id,)
    )

    conn.commit()
    conn.close()


# Update Device
def update_device(device_id, capability, feature, activity, trust_score, status):

    conn = sqlite3.connect("devices.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE devices
    SET capability=?,
        feature=?,
        activity=?,
        trust_score=?,
        status=?
    WHERE device_id=?
    """, (
        capability,
        feature,
        activity,
        trust_score,
        status,
        device_id
    ))

    conn.commit()
    conn.close()
    

# Run Database
if __name__ == "__main__":

    create_database()

    print("Database Created Successfully")