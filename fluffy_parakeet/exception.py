from fastapi import HTTPException


class BrokenCircuit(HTTPException):
    def __init__(self):
        super().__init__(status_code=403, detail="circuit has broken")
