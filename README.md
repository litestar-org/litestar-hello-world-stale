<!-- markdownlint-disable -->
<p align="center">
  <img src="https://github.com/litestar-org/branding/blob/main/assets/Branding%20-%20SVG%20-%20Transparent/Logo%20-%20Banner%20-%20Inline%20-%20Light.svg#gh-light-mode-only" alt="Litestar Logo - Light" width="100%" height="auto" />
  <img src="https://github.com/litestar-org/branding/blob/5c46ce93092faa36d0ba572f931b5d579ae75ad3/assets/Branding%20-%20SVG%20-%20Transparent/Logo%20-%20Banner%20-%20Inline%20-%20Dark.svg#gh-dark-mode-only" alt="Litestar Logo - Dark" width="100%" height="auto" />
</p>
<!-- markdownlint-restore -->

<div align="center">

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=starlite-api_starlite-hello-world&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=starlite-api_starlite-hello-world)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=starlite-api_starlite-hello-world&metric=coverage)](https://sonarcloud.io/summary/new_code?id=starlite-api_starlite-hello-world)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=starlite-api_starlite-hello-world&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=starlite-api_starlite-hello-world)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=starlite-api_starlite-hello-world&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=starlite-api_starlite-hello-world)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=starlite-api_starlite-hello-world&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=starlite-api_starlite-hello-world)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=starlite-api_starlite-hello-world&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=starlite-api_starlite-hello-world)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=starlite-api_starlite-hello-world&metric=bugs)](https://sonarcloud.io/summary/new_code?id=starlite-api_starlite-hello-world)

[![Discord](https://img.shields.io/discord/919193495116337154?color=202235&label=%20Discord&logo=discord)](https://discord.gg/X3FJqy8d2j) [![Matrix](https://img.shields.io/badge/%5Bm%5D%20Matrix-bridged-blue?color=202235)](https://matrix.to/#/#starlitespace:matrix.org) [![Reddit](https://img.shields.io/reddit/subreddit-subscribers/litestarapi?label=r%2FLitestar&logo=reddit)](https://reddit.com/r/litestarapi)

</div>

# litestar-hello-world

Minimum Litestar Implementation.

`$ poetry shell`

`$ poetry install`

`$ litestar run --reload`

`$ curl localhost:8000/ -w "\n"`

## To use for Litestar development

If you want to use this app to test a local version of `Litestar`, the litestar dependency in
`pyproject.toml` to:

```toml
litestar = {path = "../litestar", develop = true}
```

This assumes that `Litestar` and this app exist in the same directory.

Run uvicorn with:

`$ poetry run uvicorn main:app --reload --reload-dir "../litestar/litestar"`

## Code Quality

After cloning:

`$ pre-commit install`

Run on all files:

`$ pre-commit run --all-files`

Run a specific hook:

`$ pre-commit run mypy --all-files`
