# PostgreSQL Student Management Application

This is a Python application for managing student records in a PostgreSQL database.

## Prerequisites

- Python installed on your system (version 3.x)
- PostgreSQL installed and running on your system
- psycopg2 library installed (`pip install psycopg2`)

## Configuration

1. Ensure your PostgreSQL server is running.
2. Modify the database connection details (`user`, `password`, `host`, `port`, `database`) in the `create_connection()` function of the Python script according to your PostgreSQL setup.

## Steps to Compile and Run

1. Download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the Python script and the README file.

3. Run the Python script using the following command:
                                    python3 A3.py

## Interaction Options:
	After running the program, you'll see the message "Hello! Welcome to the Student Management System."
	You'll be prompted with the question "What do you want to do? (add/update/delete/getall/exit): "
	Here are the available options:
		add: Add a new student record. You'll be asked to input the student's first name, last name, email, and enrollment date.
		update: Update the email address of a student. You'll be asked to input the student ID and the new email address.
		delete: Delete a student record. You'll be asked to input the student ID of the student you want to delete.
		getall: Retrieve and display all student records.
		exit: Exit the program.

5. Link to video Demo: https://youtu.be/aT70X76KcwY
