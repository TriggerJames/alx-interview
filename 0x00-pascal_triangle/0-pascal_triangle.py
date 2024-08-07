def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
    n (int): Number of rows in Pascal's Triangle.

    Returns:
    list: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []
    
    triangle = []
    
    for i in range(n):
        if i == 0:
            row = [1]
        else:
            row = [1]
            for j in range(1, len(triangle[-1])):
                row.append(triangle[-1][j - 1] + triangle[-1][j])
            row.append(1)
        triangle.append(row)
    
    return triangle
