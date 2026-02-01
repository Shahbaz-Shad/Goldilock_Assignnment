"""Write a function to convert a decimal number string into binary string. For example, string A
contains “123” which is decimal value 123. Convert this string into binary string"""


def decimal_to_binary(decimal_str):
    try:
        num = int(decimal_str)
        if num < 0:
            raise ValueError("Negative numbers not supported")
        return bin(num)[2:]
    except ValueError as e:
        return f"Error: {e}"

num = "123"
binary_str = decimal_to_binary(num)
print(f"Decimal: {num} -> Binary: {binary_str}")
