def pascal_triangle(n):
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the top of the triangle
    triangle = [[1]]

    # Build the triangle row by row
    for i in range(1, n):
        row = [1]  # Start each row with a 1
        # Calculate the in-between values of the row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End each row with a 1
        triangle.append(row)  # Add the completed row to the triangle

    return triangle
