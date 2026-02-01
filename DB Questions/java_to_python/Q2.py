"""Write a program to read a CSV file and print the same in the output file. This csv file contains
three columns having numeric value. The output file should additionally contain the sum of
these numeric values."""

import csv

def process_csv(input_file, output_file):
    try:
        with open(input_file, newline='') as infile, open(output_file, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            header = next(reader)
            writer.writerow(header + ["sum"])

            for row in reader:
                try:
                    nums = list(map(float, row))
                    writer.writerow(nums + [sum(nums)])
                except ValueError:
                    print(f"Skipping invalid row: {row}")

    except Exception as e:
        print("Error:", e)

input_file = r'.\example_input.csv'
process_csv(input_file, 'output.csv')
