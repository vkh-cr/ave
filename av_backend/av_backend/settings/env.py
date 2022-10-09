import logging
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_DIR = BASE_DIR / "av_backend"

env = environ.Env()
env.read_env(env_file=str(BASE_DIR / ".env"))

_logger = logging.getLogger("settings")
_logger.info("BASE_DIR", BASE_DIR)
_logger.info("PROJECT_DIR", PROJECT_DIR)
