import mysql.connector
import time

# Database connection details (replace with your actual credentials)
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'advanced_db'
}

# Establish a database connection
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

def simulate_real_time_data_changes():
    try:
        while True:
            # Simulate real-time data changes
            time.sleep(5)  # Simulating a change every 5 seconds

            # Fetch the latest data from the database
            query = "SELECT * FROM students WHERE name = 'Fiona'"
            cursor.execute(query)
            results = cursor.fetchall()

            # Process the data or react to changes
            for row in results:
                print(f"Received message: {row}")

    except KeyboardInterrupt:
        print("\nExiting...")

    finally:
        # Close the database connection
        conn.close()
        print("Database connection closed")

# Start simulating real-time data changes
simulate_real_time_data_changes()