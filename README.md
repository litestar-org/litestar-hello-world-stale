<!-- markdownlint-disable -->
<img alt="Starlite logo" src="./static/starlite-banner.svg" width="100%" height="auto">
<!-- markdownlint-restore -->

<div align="center">

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=starlite-api_starlite-hello-world&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=starlite-api_starlite-hello-world)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=starlite-api_starlite-hello-world&metric=coverage)](https://sonarcloud.io/summary/new_code?id=starlite-api_starlite-hello-world)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=starlite-api_starlite-hello-world&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=starlite-api_starlite-hello-world)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=starlite-api_starlite-hello-world&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=starlite-api_starlite-hello-world)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=starlite-api_starlite-hello-world&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=starlite-api_starlite-hello-world)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=starlite-api_starlite-hello-world&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=starlite-api_starlite-hello-world)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=starlite-api_starlite-hello-world&metric=bugs)](https://sonarcloud.io/summary/new_code?id=starlite-api_starlite-hello-world)

</div>

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
