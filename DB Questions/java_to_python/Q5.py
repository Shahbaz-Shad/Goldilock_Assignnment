"""Write a program to store the value in Hashmap (key, store) and then search those given value
from the hashmap and print it.
a. Name is key and age is value so store some sample values like
i. (Ram, 36), (shyam,60)"""

def hashmap_example():
    try:
        # Creating HashMap (Dictionary)
        employee_age = {
            "Ram": 36,
            "Shyam": 60
        }

        # Value to search
        name_to_search = "Ram"

        # Searching in HashMap
        if name_to_search in employee_age:
            print(f"Name: {name_to_search}, Age: {employee_age[name_to_search]}")
        else:
            print("Name not found")

    except Exception as e:
        print("Error:", e)

hashmap_example()