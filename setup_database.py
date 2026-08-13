import mysql.connector
from mysql.connector import Error
from db_config import DB_CONFIG
from db_connection import get_connection


def create_database_and_table():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS db_students")
        cursor.execute("USE db_students")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tb_students (
                student_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                age INT NOT NULL,
                city VARCHAR(50),
                course VARCHAR(50),
                mobile VARCHAR(15),
                email VARCHAR(100) UNIQUE,
                CHECK (age > 0)
                )
        """)
        connection.commit()
        print("Database and table are ready.")
    except Error as e:
        print("Database setup error:", e)

    finally:
        if "connection" in locals() and connection.is_connected():
            cursor.close()
            connection.close()
