# -*- coding: utf-8 -*-
# -*- author: Floyda -*-

import sublime
import os

__all__ = ['get_file_path_cache', 'get_setting_path_user']


def get_file_path_cache(name):
    return os.path.join(sublime.cache_path(), 'User', '%s.cache' % name)


def get_setting_path_user(name):
    return os.path.join(sublime.packages_path(), 'User',
                        '%s.sublime-settings' % name)
