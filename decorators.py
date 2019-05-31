# -*- coding: utf-8 -*-
# -*- author: Floyda -*-

from threading import Thread
from functools import wraps


def thread(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        return Thread(target=lambda: func(*args, **kwargs)).start()

    return wrap
