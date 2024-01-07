#!/usr/bin/python3
"""

This module uses the numpy module to implement matrix multiplication

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """

    Returns product of two matrices

    Args:
    m_a (list): 1st matrix
    m_b (list): 2nd matrix

    """
    return (np.matmul(m_a, m_b))
