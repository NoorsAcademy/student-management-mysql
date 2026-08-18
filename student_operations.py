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

        print("\nStudent List")
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
    cursor = None
    connection = None
    try:
        print("\nUpdate Student")
        print_line()

        connection = get_connection()

        if connection is None:
            print("Database connection failed.")
            return

        cursor = connection.cursor()
        student_id = input("Enter Student ID to Update:")
        cursor.execute("SELECT * FROM tb_students WHERE student_id = %s",(student_id,))
        student = cursor.fetchone()
        
        if student is None:
            print("Student not Found")
            return       

        # display student details
        
        
        name = input("Enter new name: ({student[1]})").strip()
        age = int(input("Enter new age:({student[2]})")).strip()           
        city =input("Enter new city:({student[3]})").strip()
        course = input("Enter Course:({student[4]}) ").strip()
        mobile = input("Enter Mobile:({student[5]}) ").strip()
        email = input("Enter Email: ({student[6]})").strip()

        if name == "":
            name = student[1]
        if age =="":
            age = student[2]
        if city =="":
            city = student[3]
        if course =="":
            course = student[4]
        if mobile =="":
            mobile = student[5]
        if email =="":
            email = student[6]
        # do the same for other fields   
        update_query ="""
            UPDATE tb_students 
            SET name = %s,
                age = %s,
                city = %s,
                course = %s,
                mobile = %s,
                email =%s
            WHERE student_id = %s"""
        cursor.execute(update_query,(name,age,city,course,mobile,email,(student_id,)))
        connection.commit()
        print("Student Updated Successfully")
         
    except Error as e:
        print(f"Error Updating Student:",e)
        
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("Update successfully")

    


def delete_student():
    cursor = None
    connection = None
    try:
        print("\nDelete Student")
        print_line()
    
        connection = get_connection()
    
        if connection is None:
            return
        cursor = connection.cursor()

        student_id = input("Enter Student ID to delete:")
        query = """
            SELECT * FROM tb_students WHERE student_id = %s
            """
        cursor.execute(query,(student_id,))
        student = cursor.fetchone()

        if student is None:
            print("Student not found")
            return

        delete_query = "DELETE FROM tb_students WHERE student_id = %s"
        cursor.execute(delete_query,(student_id,))
        connection.commit()
        print("Student deleted successfully")

    except Error as e:
        print(f"Error Deleting Student:",e)
        
    finally:
        if cursor is not None:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()
        
