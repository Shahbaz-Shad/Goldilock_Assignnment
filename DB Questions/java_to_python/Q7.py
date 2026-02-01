"""Write a program that take the command line input and print all received input""" 

import sys

def print_command_line_inputs():
    try:
        if len(sys.argv) <= 1:
            print("No command-line arguments received")
        else:
            print("Command-line arguments:")
            for i, arg in enumerate(sys.argv[1:], start=1):
                print(f"Argument {i}: {arg}")

    except Exception as e:
        print("Error:", e)

print_command_line_inputs()

# how to run this code
# python Q7.py arg1 arg2 arg3