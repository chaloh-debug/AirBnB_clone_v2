#!/usr/bin/python3
"""compress files"""
from fabric.api import run, local, put
from datetime import datetime
import os


def do_pack():
    """ compress files and save to folder"""
    try:
        local("mkdir -p versions")
        path = ("versions/web_static_{}.tgz"
                .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
        local("tar -cvzf {} web_static".format(path))
        return path
    except Exception:
        return None
