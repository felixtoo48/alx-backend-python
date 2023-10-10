#!/usr/bin/env python3
""" collect 10 random Nos using async comprehensing and return the Nos"""
import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine will collect 10 random numbers using an
    async comprehensing over async_generator and
    return the 10 random numbers """
    random_numbers = [num async for num in async_generator()]
    return random_numbers
