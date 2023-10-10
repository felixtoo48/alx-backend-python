#!/usr/bin/env python3
""" coroutine asynchronous generator"""
import asyncio
import random


async def async_generator():
    """ loop 10 times and each time wait asynchronously for a
    second before yielding a random number """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.randint(0, 10)
