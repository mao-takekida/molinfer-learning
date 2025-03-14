"""FastAPI application entry point."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> dict:
    """Root path."""
    return {"message": "Hello, FastAPI!"}
