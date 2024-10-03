#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing Pascal's Triangle of n rows.
    Returns an empty list if n <= 0.
    """
    triangle = []

    if n <= 0:
        return triangle

    # The first row is always [1]
    triangle = [[1]]

    for row_num in range(1, n):
        # Start the new row with [1]
        row = [1]

        """
        Populate the current row
        with sums of adjacent numbers from the previous row
        """
        for col in range(1, len(triangle[row_num - 1])):
            row.append(
                triangle[row_num - 1][col - 1] + triangle[row_num - 1][col]
            )

        # End the row with [1]
        row.append(1)

        # Append the constructed row to the triangle
        triangle.append(row)

    return triangle
