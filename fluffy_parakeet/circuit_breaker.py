import time
import asyncio

from typing import Callable
from fluffy_parakeet.json_parser import json_parser
from fluffy_parakeet.exception import BreakedCircuit, Timeout

breaked_circuit = []

def circuit_breaker(destination_address):
    breaked_circuit.append(destination_address)