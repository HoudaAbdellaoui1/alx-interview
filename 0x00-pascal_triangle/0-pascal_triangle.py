def pascal_triangle(n):
    # Return an empty list if n <= 0
    if n <= 0:
        return []
    
    # Initialize the Pascal's triangle list
    triangle = []
    
    # Loop to build each row of Pascal's triangle
    for i in range(n):
        # Create a new row with 1s at both ends
        row = [1] * (i + 1)
        
        # Fill in the inner elements of the row, if applicable
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        # Add the row to the triangle
        triangle.append(row)
    
    return triangle
