import os
import sys
import time
import uvicorn
import random

from fastapi import FastAPI
from starlette.endpoints import HTTPEndpoint


class FluffyParakeet(object):
    def __init__(self):
        self.app = FastAPI()
        self.route = []

    def get_app(self):
        return self.app

    def run(self, host="127.0.0.1", port=8000):
        uvicorn.run(self.app, host=host, port=port)

    def set_route(self, routes: list):
        for route in routes:
            hash = hex(random.getrandbits(int(str(time.time())[-3:-1])))[4:]
            self.app.add_api_route(
                path=route["host"],
                endpoint=type(hash, (HTTPEndpoint, ), {})          
            )