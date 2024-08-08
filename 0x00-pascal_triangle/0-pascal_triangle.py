#!/usr/bin/python3

"""Pascal's Triangle"""


def pascal_triangle(n):
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate each row from the second to the nth
    for i in range(1, n):
        # Start the row with a '1'
        row = [1]
        # Calculate the intermediate values
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # End the row with a '1'
        row.append(1)
        # Add the row to the triangle
        triangle.append(row)

    return triangle
