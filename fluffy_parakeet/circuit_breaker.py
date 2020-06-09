import time
import asyncio

from typing import Callable
from fluffy_parakeet.json_parser import json_parser


breaked_circuit = []

async def circuit_breaker(future):
    config = json_parser("fluffy_parakeet/config.json")
    try:
        print(type(future), future)
        res = await asyncio.wait_for(future(), timeout=config["error_time"])
    except asyncio.TimeoutError:
        future.cancle()
        return None

    print(res)
    return res