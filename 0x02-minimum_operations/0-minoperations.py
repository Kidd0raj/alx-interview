#!/usr/bin/python3
'''
Minimum Operations Python3 Challenge

This script calculates the fewest number of operations needed
to result in exactly n 'H' characters in a file.

Returns:
    Integer: If n is impossible to achieve, return 0
'''

def minOperations(n):
    '''Calculates the fewest number of operations needed.

    Args:
        n (int): The desired number of 'H' characters in the file.

    Returns:
        int: The fewest number of operations needed, or 0 if impossible.
    '''
    if n <= 1:
        return 0

    clipboard = 1  # Number of 'H' characters copied
    pasted_chars = 1  # Number of characters in the file
    operations = 0  # Operations counter

    while pasted_chars < n:
        if n % pasted_chars == 0:
            # If the current number of characters in the file can evenly divide n
            clipboard = pasted_chars
            operations += 1
        pasted_chars += clipboard
        operations += 1

    return operations

# Example usage
if __name__ == "__main__":
    n = 9
    result = minOperations(n)
    print(f"Number of operations to reach {n} characters: {result}")
