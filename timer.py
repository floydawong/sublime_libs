# -*- coding: utf-8 -*-
# -*- author: Floyda -*-

from threading import Timer


class MiniTimer:
    """docstring for MiniTimer"""

    def __init__(self, interval, func):
        self.interval = interval
        self.func = func
        self.start()

    def start(self):
        self.active = True
        self.timer_handler = Timer(self.interval, self._tick)
        self.timer_handler.start()

    def _tick(self):
        if self.func:
            self.func()

        if self.active:
            self.start()

    def stop(self):
        self.active = False
