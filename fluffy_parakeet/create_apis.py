import asyncio
import aiohttp
import requests

from fastapi import Request, Response
from fluffy_parakeet.circuit_breaker import circuit_breaker, breaked_circuit
from fluffy_parakeet.json_parser import json_parser
from fluffy_parakeet.exception import BreakedCircuit


def create_api(destination_address: str, method: str):
    async def api(req: Request):
        headers = {}
        for i in req._headers._list:
            headers[i[0].decode()] = i[1].decode()

        if destination_address in breaked_circuit:
            raise BreakedCircuit

        headers["host"] = destination_address

        timeout = aiohttp.ClientTimeout(total=json_parser("fluffy_parakeet/config.json")["timeout"], )

        try:
            async with aiohttp.request(
                method=req.method, 
                url=destination_address, 
                headers=headers, 
                data=await req.body(),
                timeout=timeout) as resp:

                return await resp.text()
        except:
            circuit_breaker(destination_address)
            raise BreakedCircuit


    return api

