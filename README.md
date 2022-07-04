<img alt="Starlite logo" src="./static/starlite-banner.svg" width="100%" height="auto">

# starlite-hello-world

Minimum Starlite API Implementation.

`$ poetry install`

`$ poetry run uvicorn main:app`

`$ curl localhost:8000/ -w "\n"`

## Code Quality

After cloning:

`$ pre-commit install`

Run on all files:

`$ pre-commit run --all-files`

Run a specific hook:

`$ pre-commit run mypy --all-files`
