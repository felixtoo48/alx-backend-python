#!/usr/bin/env python3
""" collect 10 random Nos using async comprehensing and return the Nos"""
import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collects 10 random numbers using async comprehension,
    returns the 10 random numbers
    """
    result = [i async for i in async_generator()]
    return result
