import logging

import typer
import uvicorn
import uvicorn.config

from fastapi import FastAPI

from app.settings import settings

_typer = typer.Typer()
app = FastAPI()


@_typer.command()
def run_http(
    host: str = typer.Option("0.0.0.0", '--host', '-h'),
    port: int = typer.Option(8000, '--port', '-p'),
    reload: bool = typer.Option(False, '--reload'),
):

    logging.basicConfig(level=settings.log_level)
    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["access"]["fmt"] = settings.uvicorn_access_fmt
    uvicorn.run("app.main:app", host=host, port=port, reload=reload)


def main():
    _typer()


if __name__ == '__main__':
    main()
