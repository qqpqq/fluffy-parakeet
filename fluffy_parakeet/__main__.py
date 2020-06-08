import uvicorn

from fluffy_parakeet.app import FluffyParakeet


if __name__ == "__main__":
    app = FluffyParakeet()
    app.run(host="0.0.0.0")
