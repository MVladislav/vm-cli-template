import logging
import sys

import verboselogs

from ..utils.defaultLogBanner import log_runBanner
from ..utils.utils import Context, Utils

# ------------------------------------------------------------------------------
#
#
#
# ------------------------------------------------------------------------------


class TestService:

    # --------------------------------------------------------------------------
    #
    #
    #
    # --------------------------------------------------------------------------

    def __init__(self, ctx: Context):
        if ctx is not None and ctx.utils is not None:
            self.ctx: Context = ctx
            self.utils: Utils = ctx.utils
            logging.log(logging.DEBUG, "test-service is initiated")
        else:
            logging.log(logging.ERROR, "context or utils are not set")
            sys.exit(1)

    # --------------------------------------------------------------------------
    #
    #
    #
    # --------------------------------------------------------------------------

    def test(self) -> None:
        """
        ...
        """
        service_name: str = "TEST"
        log_runBanner(service_name)
        path: str = self.utils.create_service_folder(f"scan/test", None)

        self.utils.run_command_output_loop("test", [[], ["tee", f"{path}/test.log"]])

        logging.log(verboselogs.SUCCESS, f"[*] {service_name} Done! View the log reports under {path}/")
