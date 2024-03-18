import psycopg2
from psycopg2 import Error

# establish a connection to the PostgreSQL database
def create_connection():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="1312Paimana", 
            host="localhost",
            port="5432",
            database="test_db"
        )
        return connection
    except (Exception, Error) as error:
        print("Error connecting to PostgreSQL", error)

# retrieve and display all records from students table
def get_all_students(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        print("All Students:")
        for student in students:
            print(student)
    except (Exception, Error) as error:
        print("Error while fetching data from PostgreSQL", error)

#  insert a new student record into the students table
def add_student(connection, first_name, last_name, email, enrollment_date):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                       (first_name, last_name, email, enrollment_date))
        connection.commit()
        print("Student added successfully.")
    except (Exception, Error) as error:
        print("Error while adding student to PostgreSQL", error)

#  update the email address for a student with the specified student_id
def update_student_email(connection, student_id, new_email):
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET email = %s WHERE student_id = %s",
                       (new_email, student_id))
        connection.commit()
        print("Email updated successfully.")
    except (Exception, Error) as error:
        print("Error while updating email in PostgreSQL", error)

# delete the record of the student with the specified student_id
def delete_student(connection, student_id):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE student_id = %s",
                       (student_id,))
        connection.commit()
        print("Student deleted successfully.")
    except (Exception, Error) as error:
        print("Error while deleting student from PostgreSQL", error)
        
        
# Main
def main():
    # Create a connection to the PostgreSQL database
    connection = create_connection()
    
        # If connection successful
    if connection:
        # Get and display all students
        get_all_students(connection)

    # Add a new student
    add_student(connection, 'Billy', 'Bob', 'billy.bob@example.com', '2023-09-11')

    # Update email of a student
    update_student_email(connection, 1, 'john.doe.updated@example.com')

    # Delete a student
    delete_student(connection, 2)

    # Get and display all students after modifications
    get_all_students(connection)

    # Close the connection
    connection.close()


if __name__ == "__main__":
    main()
