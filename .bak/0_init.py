# -*- coding: utf-8 -*-
# -*- author: Floyda -*-

import sys
import os
from imp import reload

from .sublime_libs import log

dirname = os.path.split(os.path.dirname(__file__))[1]

all_modules = [
    # main.py
    # foo.py
    # bar.py
    # ...
]


def reload_module():
    for module in all_modules:
        name = '%s.%s' % (dirname, module)
        if name in sys.modules:
            reload(sys.modules[name])


def plugin_loaded():
    log.init(True)
    log.debug('---------- plugin_loaded ----------')
    reload_module()


def plugin_unloaded():
    log.debug('---------- plugin_unloaded ----------')
    log.clear()
