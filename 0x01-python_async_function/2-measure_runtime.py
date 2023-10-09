#!/usr/bin/env python3
""" measuring the total execution time"""
import asyncio
import random
from typing import List
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int = 10) -> float:
    """
    function with integer arguments n and max delay
    measures total execution time for wait_n
    return: total_time / n
    """
    start_time = time.perf_counter()  # Record the start time

    # Measure the total execution time for wait_n(n, max_delay)
    asyncio.run(wait_n(n, max_delay))

    end_time = time.perf_counter()  # Record the end time
    total_time = end_time - start_time

    # Calculate and return the average time per coroutine execution
    return total_time / n
