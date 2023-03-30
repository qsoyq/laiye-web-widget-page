import logging

import typer
import uvicorn
import uvicorn.config

from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.settings import settings, static_directory, templates_directory

_typer = typer.Typer()
app = FastAPI()
app.mount("/static", StaticFiles(directory=static_directory), name="static")
templates = Jinja2Templates(directory=templates_directory)


@app.get("/webwidget", response_class=HTMLResponse)
async def web_widget(request: Request, name: str = Query("", description="当前用户名称, 不传随机生成", max_length=128), env: str = Query("SKETCH", description="LC发布环境")):
    return templates.TemplateResponse("web-widget.html", {"request": request, "name": name, "env": env, **settings.dict()})


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
