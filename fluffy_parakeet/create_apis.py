import asyncio
import requests

from fastapi import Request, Response
from fluffy_parakeet.circuit_breaker import circuit_breaker


def create_api(destination_address: str, method: str):
    async def api(req: Request):
        headers = {}
        for i in req._headers._list:
            headers[i[0].decode()] = i[1].decode()

        headers["host"] = destination_address

        payload = await req.body()
        request = requests.Request(req.method, destination_address, headers=headers)
        request = request.prepare()
        request.body = payload

        async def send_data():
            s = requests.session()
            return s.send(request)

        res = await circuit_breaker(send_data)
        
        return res.text

    return api

