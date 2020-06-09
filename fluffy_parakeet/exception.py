class BreakedCircuit(Exception):
    def __str__(self):
        return "This circuit is breaked."


class Timeout(Exception):
    def __str__(self):
        return "Timeout"