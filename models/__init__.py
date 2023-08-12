#!/usr/bin/python3
from models.engine.file_storage import FileStorage

"""
This file makes python to treate diretories as packages
"""
if __name__!= "__main__":
    storage = FileStorage()
    storage.reload()