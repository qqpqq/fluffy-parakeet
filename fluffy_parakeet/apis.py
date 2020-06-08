import requests

from fastapi import Request, Response


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
        res = s.send(request)

        return res.text

    return api
