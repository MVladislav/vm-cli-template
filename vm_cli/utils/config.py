from typing import Optional, Union

from starlette.config import Config

# ------------------------------------------------------------------------------
#
#
#
# ------------------------------------------------------------------------------
config = Config(".env")
config_project = Config(".env_project")
# ------------------------------------------------------------------------------
#
#
#
# ------------------------------------------------------------------------------
PROJECT_NAME: str = config_project("PROJECT_NAME", default="vm_cli")
VERSION: str = config_project("VERSION", default="0.0.1")
ENV_MODE: str = config("ENV_MODE", default="KONS")
# CRITICAL | ERROR | SUCCESS | WARNING | NOTICE | INFO | VERBOSE | DEBUG | SPAM | NOTSET
LOGGING_LEVEL: str = config("LOGGING_LEVEL", default="DEBUG")
LOGGING_VERBOSE: int = config("LOGGING_VERBOSE", cast=int, default=0)
DEBUG: bool = True if LOGGING_LEVEL == "DEBUG" or LOGGING_LEVEL == "VERBOSE" or LOGGING_LEVEL == "SPAM" else False
DEBUG_RELOAD: bool = True if DEBUG else False
# ------------------------------------------------------------------------------
#
#
#
# ------------------------------------------------------------------------------
BASE_PATH: str = config("VM_BASE_PATH", default=f".")
# ------------------------------------------------------------------------------
#
#
#
# ------------------------------------------------------------------------------
# It is required to do a free registration and create a license key
GEO_LICENSE_KEY: Union[str, None] = config("GEO_LICENSE_KEY", default=None)
# docs: https://dev.maxmind.com/geoip/geoip2/geolite2/
GEO_LITE_TAR_FILE_URL = (
    f"https://download.maxmind.com/app/geoip_download"
    f"?edition_id=GeoLite2-City"
    f"&license_key={GEO_LICENSE_KEY}"
    f"&suffix=tar.gz"
)
# TODO: add legacy
# http://dev.maxmind.com/geoip/legacy/geolite/
GEO_DB_FNAME = "/GeoLite2-City.mmdb"
GEO_DB_ZIP_FNAME = "/GeoIP2LiteCity.tar.gz"
