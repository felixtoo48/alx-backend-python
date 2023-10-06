#!/usr/bin/env python3
"""
float multiplier and return float
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    :param multiplier: The multiplier to be used in the returned function.
    :return: A function that takes a float and returns the product.
    """
    return lambda x: x * multiplier
