#!/usr/bin/python3
"""
pascal_triangle module

This module provides functionality to generate Pascal's Triangle.

Functions:
    pascal_triangle(n): Generates a list of lists representing
    Pascal's Triangle with n rows.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        List[List[int]]: A list of lists of integers representing
        Pascal's Triangle.
        Each inner list corresponds to a row in the triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
