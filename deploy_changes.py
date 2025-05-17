import mysql.connector

# Connection details
db_user = "root"
db_password = "Secret5555"
db_name = "testdb"
host = "localhost"

# SQL statements
sql_commands = [
    "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50));",
    # We remove IF NOT EXISTS here
    "ALTER TABLE users ADD COLUMN last_login DATETIME;",
    """
    CREATE TABLE IF NOT EXISTS logs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        message TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
]

try:
    connection = mysql.connector.connect(
        host=host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = connection.cursor()

    for command in sql_commands:
        try:
            cursor.execute(command)
            print(f" Executed: {command.strip().splitlines()[0]}")
        except mysql.connector.Error as err:
            if err.errno == 1060:  # Duplicate column name
                print(f" Column already exists: {err.msg}")
            else:
                print(f" Error: {err}")

    connection.commit()
    print(" All changes deployed.")

except mysql.connector.Error as err:
    print(f" Connection error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
