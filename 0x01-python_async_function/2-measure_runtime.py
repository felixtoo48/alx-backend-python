#!/usr/bin/env python3
""" Measuring the total execution time"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int = 10) -> float:
    """ measure runtime  """
    start_time = time.time()  # Record the start time

    # Measure the total execution time for wait_n(n, max_delay)
    run(wait_n(n, max_delay))

    end_time = time.time()  # Record the end time
    total_time = end_time - start_time

    # Calculate and return the average time per coroutine execution
    return total_time / n
