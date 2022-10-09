from .base import *
from .env import env

DEBUG = False
SECRET_KEY = env.str("SECRET_KEY")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

try:
    from .local import *
except ImportError:
    pass
