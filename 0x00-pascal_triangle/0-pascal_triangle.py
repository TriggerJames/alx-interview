def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
    n (int): Number of rows in Pascal's Triangle.

    Returns:
    list: A list of lists representing Pascal's Triangle.
    """

    # Initialize the result list to hold all rows of Pascal's Triangle
    res = []

    # Only proceed if n is greater than 0
    if n > 0:
        # Iterate over each level from 1 to n
        for i in range(1, n + 1):
            # Initialize the current level as an empty list
            level = []

            # Initialize the first value in the row as 1 (C(0, 0))
            C = 1

            # Generate values for the current row
            for j in range(1, i + 1):
                # Append the current value of C to the level
                level.append(C)

                # Calculate the next value of C using the binomial coefficient formula
                C = C * (i - j) // j

            # Append the generated level to the result list
            res.append(level)

    # Return the complete Pascal's Triangle
    return res
