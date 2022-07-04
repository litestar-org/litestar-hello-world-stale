"""
Minimal Starlite application.
"""
from typing import Any

from starlite import Starlite, get


@get("/")
def hello_world() -> dict[str, Any]:
    """Hi"""
    return {"hello": "world"}


app = Starlite(route_handlers=[hello_world])
