import time
import asyncio

from typing import Callable
from fluffy_parakeet.json_parser import json_parser
from fluffy_parakeet.exception import BrokenCircuit

# temporary storage
broken_circuit = []


def circuit_breaker(destination_address):
    broken_circuit.append(destination_address)
    # TODO
    # circuit break system
