import logging

from pydantic import BaseSettings


class Settings(BaseSettings):

    uvicorn_access_fmt: str = '%(levelprefix)s %(asctime)s - %(client_addr)s - "%(request_line)s" - %(status_code)s'
    debug: bool = True
    log_level: int = logging.DEBUG


settings = Settings()
