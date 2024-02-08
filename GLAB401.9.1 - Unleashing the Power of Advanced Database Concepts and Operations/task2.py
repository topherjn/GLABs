import mysql.connector

# Establish a database connection
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="advanced_db"
    )
    cursor = conn.cursor()
    print("Connected to MySQL database successfully\n")
except mysql.connector.Error as e:
    print(f"Error: {e}")
    exit(1)

# Batch Insert Operation
try:
    batch_insert_query = "INSERT INTO students (name, age) VALUES (%s, %s)"
    data_to_insert = [
        ("Fiona", 18),
        ("George", 20),
        ("Helen", 22),
        ("Ivan", 21),
        ("Julia", 19),
    ]
    cursor.executemany(batch_insert_query, data_to_insert)
    conn.commit()
    print("Batch insert operation completed successfully\n")
except mysql.connector.Error as e:
    print(f"Error: {e}")
    conn.rollback()

# Batch Update Operation
try:
    batch_update_query = "UPDATE students SET age = %s WHERE name = %s"
    data_to_update = [
        (25, "George"),
        (24, "Helen"),
    ]
    cursor.executemany(batch_update_query, data_to_update)
    conn.commit()
    print("Batch update operation completed successfully\n")
except mysql.connector.Error as e:
    print(f"Error: {e}")
    conn.rollback()

# Batch Delete Operation
try:
    batch_delete_query = "DELETE FROM students WHERE name = %s"
    names_to_delete = [("Ivan",), ("Julia",)]
    cursor.executemany(batch_delete_query, names_to_delete)
    conn.commit()
    print("Batch delete operation completed successfully\n")
except mysql.connector.Error as e:
    print(f"Error: {e}")
    conn.rollback()

# Close the database connection
conn.close()
print("Database connection closed")