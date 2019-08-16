# -*- coding: utf-8 -*-
# -*- author: Floyda -*-

import sublime
from sublime_lib import SettingsDict, NamedSettingsDict

import os
import json
from .resource import get_cache_file_path, get_user_setting_path


class Storage:
    def __init__(self, name):
        self._name = name
        self._dict = {}

    def save(self):
        pass

    def clear(self):
        pass

    def set(self, key, value):
        self._dict[key] = value

    def get(self, key, default=None):
        return self._dict.get(key, default)

    def get_items(self):
        return self._dict.items()

    def get_keys(self):
        return self._dict.keys()


class StorageSetting(Storage):
    def __init__(self, name):
        super(StorageSetting, self).__init__(name)
        self._dict = NamedSettingsDict(name)

    def save(self):
        self._dict.save()

    def clear(self):
        self._dict.update({})
        self._dict.save()


class StorageCache(Storage):
    def __init__(self, name):
        super(StorageCache, self).__init__(name)
        self._path = get_cache_file_path(self._name)
        self._dict = {}
        self._load()

    def _load(self):
        try:
            fp = open(self._path)
            content = fp.read()
            fp.close()
            self._dict = json.loads(content)
        except:
            self.clear()

    def save(self):
        try:
            fp = open(self._path, "w+")
            print("save content:", json.dumps(self._dict))
            fp.write(json.dumps(self._dict))
            fp.close()
        except:
            sublime.error_message("Cann't save to local.")

    def clear(self):
        self._dict = {}
        try:
            fp = open(self._path, "w+")
            fp.write("{}")
            fp.close()
        except:
            sublime.error_message("Cann't save to local.")
