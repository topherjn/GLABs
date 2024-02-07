""" Task 1: Database Connection"""

# connector already installed, will use it here to create
# operations_db database

# create connector object
import mysql.connector
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
       
    )

except mysql.connector.Error as e:
    print(f"Error: {e}")

# build create db command
query = 'CREATE DATABASE IF NOT EXISTS operations_db'

# create the cursor object for the connectoin
cursor = conn.cursor()

# execute the command
cursor.execute(query)

# being using this db
cursor.execute("USE operations_db")

"""Task 2: CRUD Operations"""

# Create table
try:
    cursor = conn.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS students (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(50),
        age INT,
        PRIMARY KEY (id)
    )    
    """
    cursor.execute(create_table_query)
    print("Table 'students' created successfully")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    cursor.close()

# Create data
try:
    cursor = conn.cursor()

    insert_data_query = """INSERT INTO students (name, age) VALUES ("Joe", 22) """

    cursor.execute(insert_data_query)
    conn.commit()
    print("Data inserted successfully")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    cursor.close()


# Read
