# -*- coding: utf-8 -*-
# -*- author: Floyda -*-

import sublime
import os

__all__ = [
    "get_cache_file_path",
    "get_user_setting_path",
    "get_user_project_path",
    "get_user_path",
    "get_executable_path",
]


def get_cache_file_path(name):
    return os.path.join(sublime.cache_path(), "User", "%s.cache" % name)


def get_user_path():
    return os.path.join(sublime.packages_path(), "User")


def get_user_setting_path(name):
    return os.path.join(get_user_path(), "%s.sublime-settings" % name)


def get_user_project_path(name):
    return os.path.join(get_user_path(), "%s.sublime-project" % name)


def get_executable_path():
    """get sublime executable path"""
    executable_path = sublime.executable_path()
    if sublime.platform() == "osx":
        app_path = executable_path[: executable_path.rfind(".app/") + 5]
        executable_path = app_path + "Contents/SharedSupport/bin/subl"
    return executable_path
