import logging
import sys

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
            logging.log(logging.DEBUG, 'test-service is initiated')
        else:
            logging.log(logging.ERROR, "context is not set")
            sys.exit(1)

    # --------------------------------------------------------------------------
    #
    #
    #
    # --------------------------------------------------------------------------

    def test(self):
        try:
            pass
        except Exception as e:
            logging.log(logging.CRITICAL, e, exc_info=True)
