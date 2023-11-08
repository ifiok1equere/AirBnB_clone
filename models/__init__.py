#!/usr/bin/python3
'''This module creates unique instances of FileStorage
'''

from .engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
