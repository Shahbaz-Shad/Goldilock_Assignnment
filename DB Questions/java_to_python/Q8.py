"""Write a SQL query to find the age is less than 30 and name start with S"""

import mysql.connector

def get_employees():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="test"
        )

        cursor = conn.cursor()
        query = """
        SELECT emp_name, emp_age
        FROM test
        WHERE emp_age < %s
          AND emp_name LIKE %s
        """

        cursor.execute(query, (30, 'S%'))
        results = cursor.fetchall()

        for name, age in results:
            print(f"Name: {name}, Age: {age}")

    except mysql.connector.Error as e:
        print("Database Error:", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

get_employees()

# to test this code, ensure you have a MySQL database set up with the appropriate table and data.
