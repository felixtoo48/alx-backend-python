#!/usr/bin/env python3
"""
function that takes input list of floats and return
their sum in float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculates the sum of the elements in a list of floats.

    :param input_list: The input list of floats.
    :return: The sum of the elements in the input list as a float.
    """
    return sum(input_list)
