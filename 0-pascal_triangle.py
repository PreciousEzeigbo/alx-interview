def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    # Create each row of the triangle
    for i in range(n):
        # Start the row with 1
        row = [1] * (i + 1)
        
        # Compute the values inside the row by summing the two numbers from the previous row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        # Add the row to the triangle
        triangle.append(row)
    
    return triangle