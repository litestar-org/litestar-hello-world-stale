"""Minimal Starlite application."""
from typing import Any

from starlite import Starlite, get


@get("/")
def hello_world() -> dict[str, Any]:
    """Route Handler that outputs hello world."""
    return {"hello": "world"}


app = Starlite(route_handlers=[hello_world])
