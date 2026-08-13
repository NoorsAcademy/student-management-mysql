from setup_database import create_database_and_table
from student_operations import (
    add_student,
    view_students,
    search_student_by_city,
    update_student,
    delete_student
)

def main_menu():
    create_database_and_table()

    while True:
        print("\n")
        print("=" * 50)
        print("Student Management System")
        print("=" * 50)
        print("1. Add Student")
        print("2. View Students")      
        print("3. Search Students by City")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student_by_city()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Thank you.")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()

"""
student-management-mysql

main.py
db_config.py
db_config_example.py 
db_connection.py
setup_database.py
student_operations.py
.gitignore

"""