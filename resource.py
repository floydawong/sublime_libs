# -*- coding: utf-8 -*-
# -*- author: Floyda -*-

import sublime
import os

__all__ = ["get_cache_file_path", "get_user_setting_path", "get_user_project_path"]


def get_cache_file_path(name):
    return os.path.join(sublime.cache_path(), "User", "%s.cache" % name)


def get_user_setting_path(name):
    return os.path.join(sublime.packages_path(), "User", "%s.sublime-settings" % name)


def get_user_project_path(name):
    return os.path.join(sublime.packages_path(), "User", "%s.sublime-project" % name)
