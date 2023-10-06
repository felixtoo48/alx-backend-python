#!/usr/bin/env python3
"""
function’s parameters and return values with the appropriate types
"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Calculates the length of each element in the input list and
    returns a list of tuples.

    :param lst: The input list of strings.
    :return: A list of tuples, where each tuple contains a
    string from the input list
             and its corresponding length as an integer.
    """
    return [(i, len(i)) for i in lst]
