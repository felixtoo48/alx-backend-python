#!/usr/bin/env python3
"""
takes mixed list of integers and floats and return
sum in float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of the elements in a list of integers and floats.

    :param mxd_lst: The input list of integers and floats.
    :return: The sum of the elements in the input list as a float.
    """
    return sum(mxd_lst)
