# rmrl-aas
*reMarkable Rendering Library - as a Service*


[![Actions Status](https://github.com/tmsmr/rmrl-aas/workflows/Docker/badge.svg)](https://github.com/tmsmr/rmrl-aas/actions)


## What is this?
This is basically a wrapper for [@rschroll](https://www.github.com/rschroll)'s `rmrl` Python package (https://github.com/rschroll/rmrl) to make the `render` call available via HTTP. So, whole credits go to him - I just put things together 😀.

## WARNING
There are NO security checks / validations whatsoever. This service is NOT intended to be hosted publicly!

## Run
### Python / `pip`
- Install dependencies: `pip install -r requirements`
- Run: `waitress-serve --host=127.0.0.1 rmrl_aas:app`

### Docker
- Build image: `docker build -t rmrl-aas .`
- Run: `docker run -d -p 127.0.0.1:8080:8080 rmrl-aas`
- Or use the prebuilt image ([GitHub Workflow](.github/workflows/docker-publish.yml)): `docker run -d -p 127.0.0.1:8080:8080 ghcr.io/tmsmr/rmrl-aas:v0.2.1`

## Use
`curl -X POST -F file=@xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx.zip localhost:8080/render -o xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx.pdf`

**Yes, the file is submitted as form input!**

*Or, use your favorite programming language to build a client...*

*Or, use the minimal Web-GUI at `localhost:8080/` for tryout purposes...*
