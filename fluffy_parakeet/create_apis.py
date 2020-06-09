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
        
        s = requests.session()

        # res = circuit_breaker(s.send(request))
        res = s.send(request)

        return res.text

    return api
