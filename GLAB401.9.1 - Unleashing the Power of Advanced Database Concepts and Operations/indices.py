import mysql.connector

# Establish a database connection
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
    )
    cursor = conn.cursor()
    print("Connected to MySQL database successfully\n")
except mysql.connector.Error as e:
    print(f"Error: {e}")
    exit(1)

# create and use new db
query = "CREATE DATABASE IF NOT EXISTS advanced_db"

try:
    cursor.execute(query)
except mysql.connector.Error as e:
    print(f"Error: {e}")

query = "USE advanced_db"

try:
    cursor.execute(query)
except mysql.connector.Error as e:
    print(f"Error: {e}")


# Create a table without secondary index
try:
    create_table_query = """
    CREATE TABLE IF NOT EXISTS students (
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT
    )
    """
    cursor.execute(create_table_query)
    print("Table 'students' created successfully")
except mysql.connector.Error as e:
    print(f"Error: {e}")

# Insert sample data
try:
    insert_data_query = "INSERT INTO students (name, age) VALUES (%s, %s)"
    data_to_insert = [
        ("Alice", 20),
        ("Bob", 22),
        ("Charlie", 21),
        ("David", 23),
        ("Eva", 19),
    ]
    cursor.executemany(insert_data_query, data_to_insert)
    conn.commit()
    print("Data inserted successfully\n")
except mysql.connector.Error as e:
    print(f"Error: {e}")
    conn.rollback()

# Create a secondary index on the 'age' column
try:
    create_index_query = "CREATE INDEX idx_age ON students (age)"
    cursor.execute(create_index_query)
    print("Secondary index on 'age' column created successfully")
except mysql.connector.Error as e:
    print(f"Error: {e}")

# Query without secondary index (inefficient)
try:
    query_without_index = "SELECT * FROM students WHERE age = 21"
    cursor.execute(query_without_index)
    result = cursor.fetchall()
    print("Query result without secondary index:")
    for row in result:
        print(row)
except mysql.connector.Error as e:
    print(f"Error: {e}")

# Query with secondary index (improved performance)
try:
    query_with_index = "SELECT * FROM students WHERE age = 21"
    cursor.execute(query_with_index)
    result = cursor.fetchall()
    print("\nQuery result with secondary index:")
    for row in result:
        print(row)
except mysql.connector.Error as e:
    print(f"Error: {e}")

# Close the database connection
conn.close()
print("\nDatabase connection closed")

