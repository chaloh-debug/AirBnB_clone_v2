#!/usr/bin/python3
"""deploy module"""
from fabric.api import *
from os.path import exists


env.user = "ubuntu"
env.hosts = ["3.95.32.122", "18.207.140.67"]


def do_deploy(archive_path):
    """deploy to server"""
    if not exists(archive_path):
        return False
    try:
        file = archive_path.split("/")[-1]
        name = file.split(".")[0]

        new_path = "/data/web_static/releases/{}/".format(name)
        tmp_path = "/tmp/{}".format(file)

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(new_path))
        run("tar -xzf {} -C {}".format(tmp_path, new_path))
        run("rm {}".format(tmp_path))
        run("mv {}web_static/* {}".format(new_path, new_path))
        run("rm -rf {}web_static".format(new_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(new_path))
        print("New version deployed!")
        return True
    except Exception:
        return False
