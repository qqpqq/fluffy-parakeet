import os
import sys
import time
import uvicorn
import random
import requests

from fluffy_parakeet.apis import create_api
from fastapi import FastAPI
from starlette.endpoints import HTTPEndpoint
from fluffy_parakeet.json_parser import json_parser


class FluffyParakeet(object):
    def __init__(self) -> None:
        self.app: FastAPI = FastAPI()
        self.routes: list = json_parser("fluffy_parakeet/route.json")

    def get_app(self) -> FastAPI:
        return self.app

    def run(self, host="127.0.0.1", port=8000) -> None:
        self.register_routes(self.routes)

        uvicorn.run(self.app, host=host, port=port)

    def register_routes(self, routes: list) -> None:
        for route in routes:
            hash = hex(random.getrandbits(int(str(time.time())[-3:-1])))[4:]
            api = create_api(route["d_address"], route["d_method"])

            self.app.add_api_route(
                path=route["path"],
                endpoint=type(hash, (HTTPEndpoint,), {"api": api}).api,
                methods=route["methods"],
            )
