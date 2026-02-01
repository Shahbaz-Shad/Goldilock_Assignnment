"""Write a program to read value from the DB. The SB scheme is as follows:
a. Username: root
b. Password: root
c. Table name: test
d. Schema
i. Emp name varchar 200
ii. Emp age int 10
"""

import mysql.connector

def read_from_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="test"
        )

        cursor = connection.cursor()
        query = "SELECT emp_name, emp_age FROM test"
        cursor.execute(query)

        records = cursor.fetchall()

        for emp_name, emp_age in records:
            print(f"Employee Name: {emp_name}, Age: {emp_age}")

    except mysql.connector.Error as e:
        print("Database Error:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

read_from_db()
