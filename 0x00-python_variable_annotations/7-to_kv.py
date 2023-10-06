#!/usr/bin/env python3
"""
7 returns a tuple of k and v arguments
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple with the string 'k' and the square of 'v' as a float.

    :param k: The input string.
    :param v: The input integer or float.
    :return: A tuple containing 'k' and the square of 'v' as a float.
    """
    squared_value = float(v) ** 2
    return k, squared_value
