""""Write a program to find the multiple occurrences of same value in the file. A csv file contain column, say col1, col2, col3. You need to find the count of records which has the same value of col3."""


import csv
from collections import Counter

def count_col3_occurrences(input_file):
    try: 
        with open(input_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)  # read with header
            col3_values = [row['col3'] for row in reader]

        # Count occurrences
        counts = Counter(col3_values)

        # Print results
        print("Occurrences of each value in col3:")
        for value, count in counts.items():
            print(f"{value}: {count}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
    except KeyError:
        print("Error: 'col3' column not found in the CSV")
    except Exception as e:
        print("Error:", e)

input_file = r"input_example_Q10.csv"
count_col3_occurrences(input_file)
