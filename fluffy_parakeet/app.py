import os
import sys
import time
import uvicorn
import random
import requests

from fluffy_parakeet.apis import api
from fastapi import FastAPI
from starlette.endpoints import HTTPEndpoint


class FluffyParakeet(object):
    def __init__(self):
        self.app = FastAPI()
        self.route = []

    def get_app(self):
        return self.app

    def run(self, host="127.0.0.1", port=8000):
        self.set_route([{"address":"/", "methods":["GET"]},{"address":"/test", "methods":["POST"]}])
        uvicorn.run(self.app, host=host, port=port)

    def set_route(self, routes: list):
        for route in routes:
            hash = hex(random.getrandbits(int(str(time.time())[-3:-1])))[4:]
            self.app.add_api_route(
                path = route["address"],
                endpoint = type(hash, (HTTPEndpoint,), {"api": api}).api,
                methods = route["methods"]
            )