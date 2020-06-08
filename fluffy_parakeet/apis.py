from fastapi import Request


def create_api(destination_address: str, method: str):
    async def api(request: Request):
        return {
            "header": request.headers.raw,
            "body": request.body
            }

    return api
