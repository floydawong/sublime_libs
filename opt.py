# -*- coding: utf-8 -*-
# -*- author: Floyda -*-
# operation

import sublime
import os

__all__ = ["edit_settings"]


def edit_settings(base_setting_path):
    sublime.run_command(
        "edit_settings", {"base_file": base_setting_path, "default": "{\n\t$0\n}\n"}
    )
