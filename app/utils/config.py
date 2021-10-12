from pathlib import Path

from starlette.config import Config

# ------------------------------------------------------------------------------
#
#
#
# ------------------------------------------------------------------------------

config = Config(".env")

# ------------------------------------------------------------------------------
#
#
#
# ------------------------------------------------------------------------------


LICENSE: str = config("LICENSE", default="GNU AGPLv3")
AUTHOR: str = config("AUTHOR", default="MVladislav")
AUTHOR_EMAIL: str = config("AUTHOR_EMAIL", default="info@mvladislav.online")

PROJECT_NAME: str = config("PROJECT_NAME", default="Project Name")
ENV_MODE: str = config("ENV_MODE", default="KONS")
VERSION: str = config("VERSION", default="0.0.1")

# NOTICE | SPAM | DEBUG | VERBOSE | INFO | NOTICE | WARNING | SUCCESS | ERROR | CRITICAL
LOGGING_LEVEL: str = config("LOGGING_LEVEL",  default="DEBUG")
LOGGING_VERBOSE: int = config("LOGGING_VERBOSE", cast=int,  default=2)
DEBUG: bool = True if LOGGING_LEVEL == "DEBUG" or \
    LOGGING_LEVEL == "VERBOSE" or LOGGING_LEVEL == "SPAM" else False
DEBUG_RELOAD: bool = True if DEBUG else False

# ------------------------------------------------------------------------------
#
#
#
# ------------------------------------------------------------------------------


BASE_PATH: str = config("VM_BASE_PATH", default=f'{Path.home()}/Documents/{PROJECT_NAME}')
