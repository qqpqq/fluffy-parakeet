import os
import sys
import time
import uvicorn
import random
import requests

from fluffy_parakeet.apis import create_api
from fastapi import FastAPI
from starlette.endpoints import HTTPEndpoint


class FluffyParakeet(object):
    def __init__(self):
        self.app = FastAPI()
        self.route = []

    def get_app(self):
        return self.app

    def run(self, host="127.0.0.1", port=8000):
        self.set_route([{"path":"/", "methods":["GET"],"d_address":"http://www.naver.com"},{"path":"/test", "methods":["POST"], "d_address":"http://www.naver.com"}])
        uvicorn.run(self.app, host=host, port=port)

    def set_route(self, routes: list):
        for route in routes:
            hash = hex(random.getrandbits(int(str(time.time())[-3:-1])))[4:]
            api = create_api(route["d_address"])

            self.app.add_api_route(
                path = route["path"],
                endpoint = type(hash, (HTTPEndpoint,), {"api": api}).api,
                methods = route["methods"]
            )