import logging

from pathlib import Path

from pydantic import BaseSettings

import app


class Settings(BaseSettings):

    uvicorn_access_fmt: str = '%(levelprefix)s %(asctime)s - %(client_addr)s - "%(request_line)s" - %(status_code)s'
    debug: bool = True
    log_level: int = logging.DEBUG

    publicAssetsPath: str
    agentId: str
    channelId: str
    serviceAccountId: str
    serviceAccountSecret: str
    baseUrl: str
    sdk_src: str
    historyChannelId: str = '2'
    background_image: str = '/static/bg_img.png'


settings = Settings() # type: ignore

static_directory = (Path(list(app.__path__)[0]) / 'static').absolute()
templates_directory = (Path(list(app.__path__)[0]) / 'templates').absolute()
