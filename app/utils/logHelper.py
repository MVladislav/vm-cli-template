import logging
from enum import Enum

import coloredlogs
import verboselogs

from ..utils.config import LOGGING_LEVEL, LOGGING_VERBOSE


class LoggingMsgType(Enum):
    NOT_EMPTY = "NOT_EMPTY"
    EMPTY = "EMPTY"
    EXCEPTION = "EXCEPTION"


def loggingMsgHandler(type: LoggingMsgType) -> str:
    if type == LoggingMsgType.NOT_EMPTY:
        return "the value is not empty"
    elif type == LoggingMsgType.EMPTY:
        return "the value is empty"
    elif type == LoggingMsgType.EXCEPTION:
        return "internal error appears"
    else:
        return None


class LogHelper:

    # --------------------------------------------------------------------------
    #
    #
    #
    # --------------------------------------------------------------------------

    def __init__(self):
        # configure logger for requested verbosity
        if LOGGING_VERBOSE >= 4:
            log_format = '[%(asctime)s,%(msecs)03d] %(name)s[%(process)d] {%(lineno)-6d: (%(funcName)-30s)} %(levelname)-7s - %(message)s'
        elif LOGGING_VERBOSE >= 3:
            log_format = '[%(filename)-18s/%(module)-15s - %(lineno)-6d: (%(funcName)-30s)]:: %(levelname)-7s - %(message)s'
        elif LOGGING_VERBOSE >= 2:
            log_format = '%(levelname)-7s - %(message)s ac'
        elif LOGGING_VERBOSE >= 1:
            log_format = '%(levelname)-7s - %(message)s'
        elif LOGGING_VERBOSE >= 0:
            log_format = '%(message)s'
        elif LOGGING_VERBOSE < 0:
            log_format = '%(message)s'

        # create a log objectfrom verboselogs
        verboselogs.install()

        for logger_name in [logging.getLogger()] + \
                [logging.getLogger(name) for name in logging.root.manager.loggerDict]:
            for handler in logger_name.handlers:
                logger_name.removeHandler(handler)
            # # define an handle
            # logger_name.addHandler(logging.StreamHandler())
            # define log level default
            logger_name.setLevel(logging.getLevelName(LOGGING_LEVEL))
            # add colered logs
            coloredlogs.install(
                level=logging.getLevelName(LOGGING_LEVEL),
                fmt=log_format,
                logger=logger_name
            )

        # # add colered logs
        # coloredlogs.install(level=logging.getLevelName(LOGGING_LEVEL), fmt=log_format)
