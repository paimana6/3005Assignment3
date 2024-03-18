import psycopg2
from psycopg2 import Error

# establish a connection to the PostgreSQL database
def create_connection():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="shhhh",
            host="localhost",
            port="5432",
            database="test_db"
        )
        return connection
    except (Exception, Error) as error:
        print("Error connecting to PostgreSQL:", error)
        return None

# retrieve and display all records from students table
def get_all_students(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students ORDER BY student_id")
        students = cursor.fetchall()
        if students:
            print("All Students:")
            for student in students:
                print(student)
        else:
            print("No students found.")
    except (Exception, Error) as error:
        print("Error while fetching data from PostgreSQL:", error)

# insert a new student record into the students table
def add_student(connection, first_name, last_name, email, enrollment_date):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                       (first_name, last_name, email, enrollment_date))
        connection.commit()
        print("Student added successfully.")
    except (Exception, Error) as error:
        print("Error while adding student:", error)

# update the email address for a student with the specified student_id
def update_student_email(connection, student_id, new_email):
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET email = %s WHERE student_id = %s",
                       (new_email, student_id))
        if cursor.rowcount == 0:
            print("No student found with the specified ID.")
        else:
            connection.commit()
            print("Email updated successfully.")
    except (Exception, Error) as error:
        print("Error while updating email:", error)

# delete the record of the student with the specified student_id
def delete_student(connection, student_id):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE student_id = %s",
                       (student_id,))
        if cursor.rowcount == 0:
            print("No student found with the specified ID.")
        else:
            connection.commit()
            print("Student deleted successfully.")
    except (Exception, Error) as error:
        print("Error while deleting student:", error)


# Main
def main():
    print("Hello! Welcome to the Student Management System.")
    while True:
        # Create a connection to the PostgreSQL database
        connection = create_connection()

        # If connection successful
        if connection:
            # Ask the user for the action they want to perform
            action = input("\nWhat do you want to do? (add/update/delete/getall/exit): ").strip().lower()

            # Perform the chosen action
            if action == 'add':
                first_name = input("Enter first name: ").strip()
                last_name = input("Enter last name: ").strip()
                email = input("Enter email: ").strip()
                enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ").strip()
                add_student(connection, first_name, last_name, email, enrollment_date)

            elif action == 'update':
                student_id = input("Enter student ID to update: ").strip()
                new_email = input("Enter new email: ").strip()
                update_student_email(connection, student_id, new_email)

            elif action == 'delete':
                student_id = input("Enter student ID to delete: ").strip()
                delete_student(connection, student_id)

            elif action == 'getall':
                get_all_students(connection)

            elif action == 'exit':
                print("\nGoodbye!")
                break  # Exit the loop

            else:
                print("\nSorry, I didn't understand that action. Please try again.")

            # Close the connection
            connection.close()


if __name__ == "__main__":
    main()

