import time
import asyncio

from typing import Callable
from fluffy_parakeet.json_parser import json_parser


async def circuit_breaker(future: Callable):
    config = json_parser("fluffy_parakeet/config")
    try:
        asyncio.wait_for(future, timeout=config["error_time"])
    except asyncio.TimeoutError:
        return False
    return True 