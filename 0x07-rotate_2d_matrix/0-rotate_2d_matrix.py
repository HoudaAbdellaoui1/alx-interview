#!/usr/bin/python3
""" ROTATE 2D MATRIC"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.
    
    Args:
        matrix (List[List[int]]): The 2D matrix to rotate.
        
    Returns:
        None: The matrix is modified in-place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()
