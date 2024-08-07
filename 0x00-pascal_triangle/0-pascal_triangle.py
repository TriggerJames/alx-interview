#!/usr/bin/python3
 """
    Generate Pascal's Triangle up to the nth row.

    Args:
    n (int): Number of rows in Pascal's Triangle.

    Returns:
    list: A list of lists representing Pascal's Triangle.
    """

def pascal_triangle(n):
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            res.append(level)
    return res
