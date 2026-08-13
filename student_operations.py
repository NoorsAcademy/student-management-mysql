from mysql.connector import Error
from db_connection import get_connection


def print_line():
    print("-" * 70)


def add_student():
    try:
        print("\n Add Student")
        print_line()

        name = input("Enter Name: ").strip()
        age = int(input("Enter Age: "))
        city = input("Enter City: ").strip()
        course = input("Enter Course: ").strip()
        mobile = input("Enter Mobile: ").strip()
        email = input("Enter Email: ").strip()

        if name == "":
            print("Name cannot be empty.")
            return
        if email == "":
            email = None

        connection = get_connection()

        if connection is None:
            return

        cursor = connection.cursor()

        query = """
            INSERT INTO tb_students 
            (name, age, city, course, mobile, email)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (name, age, city, course, mobile, email)
        
        cursor.execute(query, values)
        connection.commit()
    

        print("Student added successfully.")
        print("New Student ID:", cursor.lastrowid)
    except Error as e:
        print("Error adding student.", e)
    finally:
        if "connection" in locals() and connection is not None and connection.is_connected():
            cursor.close()
            connection.close()


def view_students():
    try:
        connection = get_connection()

        if connection is None:
            return
        cursor = connection.cursor()

        query = """
            SELECT student_id, name, age, city, course, mobile, email
            FROM tb_students
            ORDER BY student_id
        """

        cursor.execute(query)
        students = cursor.fetchall()

        if len(students) == 0:
            print("No students found.")
            return

        print("\Student List")
        print_line()

        for student in students:
            print(f"Student ID: {student[0]}")
            print(f"Name: {student[1]}")
            print(f"Age: {student[2]}")
            print(f"City: {student[3]}")
            print(f"Course: {student[4]}")
            print(f"Mobile: {student[5]}")
            print(f"Email: {student[6]}")
    except Error as e:
        print("Error viewing studetns:, e")
    finally:
        if "connection" in locals() and connection is not None and connection.is_connected():
            cursor.close()
            connection.close()


def search_student_by_city():
    print("Search Students by City module coming soon")
    # to be completed by Abu


def update_student():
    print("Update Student module coming soon")
    # to be completed by Zeenath


def delete_student():
    print("Delete Student module coming soon")
    # to be completed by Zeenath
