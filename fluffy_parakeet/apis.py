import requests

def create_api(destination_address: str, method: str):
    async def api():
        return requests.get(destination_address).text

    return api