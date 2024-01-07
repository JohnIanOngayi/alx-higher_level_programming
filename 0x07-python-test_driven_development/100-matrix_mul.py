#!/usr/bin/python3
"""

This module contains a function that multiplies 2 matrices

"""


def matrix_mul(m_a, m_b):
    """

    Multiplies two matrices

    Args:
    m_a (list): the first matrix
    m_b (list): the second matrix

    Raises:
    TypeError: if either m_a or m_b is not a list of lists of numerics
                or if number of elements in all nested lists is not equal
    ValueError: if either m_a or m_b is empty

    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
    for i in m_b:
        if not isinstance(i, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0:
        raise ValueError("m_a cannot be empty")
    for i in range(0, len(m_a)):
        if len(m_a[i]) == 0:
            raise ValueError("m_a cannot be empty")
        for j in m_a[i]:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("m_a should contain only integers or floats")
        if len(m_a[i]) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    if len(m_b) == 0:
        raise ValueError("m_b cannot be empty")
    for i in range(0, len(m_b)):
        if len(m_b[i]) == 0:
            raise ValueError("m_b cannot be empty")
        for j in m_b[i]:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("m_b should contain only integers or floats")
        if len(m_b[i]) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    M = len(m_a)
    N = len(m_a[0])
    P = len(m_b[0])

    result = []
    for i in range(M):
        row = []
        for j in range(P):
            row.append(0)
        result.append(row)

    for i in range(M):
        for j in range(P):
            for k in range(N):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
