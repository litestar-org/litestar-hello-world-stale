<img alt="Starlite logo" src="./static/starlite-banner.svg" width="100%" height="auto">

# starlite-hello-world

Minimum Starlite API Implementation.

`$ poetry install`

`$ poetry run uvicorn main:app --reload`

`$ curl localhost:8000/ -w "\n"`

## To use for Starlite development

If you want to use this app to test a local version of `Starlite`, the starlite dependency in
`pyroject.toml` to:

```toml
starlite = {path = "../starlite", develop = true}
```

This assumes that `Starlite` and this app exist in the same directory.

Run uvicorn with:

`$ poetry run uvicorn main:app --reload --reload-dir "../starlite/starlite"`

## Code Quality

After cloning:

`$ pre-commit install`

Run on all files:

`$ pre-commit run --all-files`

Run a specific hook:

`$ pre-commit run mypy --all-files`
