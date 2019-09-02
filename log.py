# -*- coding: utf-8 -*-
# -*- author: Floyda -*-

import os
import logging

__all__ = ["init", "clear", "debug", "info", "warning", "error", "critical"]

PROJ_NAME = os.path.split(os.path.split(os.path.dirname(__file__))[0])[1]
logger = logging.getLogger(PROJ_NAME)
handler = None


def _add_handler():
    global handler
    handler = logging.StreamHandler()
    formatter = logging.Formatter("[{}] %(message)s".format(PROJ_NAME))
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def _remove_handler():
    global handler
    logger.removeHandler(handler)
    handler = None


def init(show_debug=False):
    if show_debug:
        logger.setLevel(logging.DEBUG)
        _add_handler()
        return
    logger.setLevel(logging.CRITICAL + 1)


def clear():
    _remove_handler()


def _m(prefix, msg):
    """Messages To String"""
    return "{}: ".format(prefix) + " ".join([str(x) for x in msg])


def debug(*msg):
    logger.debug(_m("debug", msg))


def info(*msg):
    logger.info(_m("info", msg))


def warning(*msg):
    logger.warning(_m("warning", msg))


def error(*msg):
    logger.error(_m("error", msg))


def critical(*msg):
    logger.critical(_m("critical", msg))


if __name__ == "__main__":
    # init()
    init(True)
    debug("debug")
    info("info")
    warning("warning")
    error("error")
    critical("critical")
    clear()
