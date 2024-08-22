#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    Calculate the minimum number of operations
    needed to obtain exactly 'n' 'H' characters
    in a text editor, starting with one 'H' and
    using only two operations: "Copy All" and "Paste".

    Args:
    n (int): The desired number of 'H' characters.

    Returns:
    int: The minimum number of operations required
    to achieve exactly 'n' 'H' characters.
    If `n` is less than or equal to 1, returns
    0 as it is impossible to achieve.
    """

    if n <= 1:
        return 0

    operations = 0  # Initialize the count of operations
    divisor = 2  # Start with the smallest possible divisor

    # Factorize the number `n` by dividing it by the smallest possible divisor
    while n > 1:
        # While n is divisible by the current divisor
        while n % divisor == 0:
            operations += divisor  # Add the divisor to the operations count
            n //= divisor  # Divide n by the divisor
        divisor += 1  # Move to the next potential divisor

    return operations  # Return the total number of operations required
