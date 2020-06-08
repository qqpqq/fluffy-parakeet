import requests

def create_api(destination_address):
    async def api():
        return requests.get(destination_address).text

    return api