#!/usr/bin/python3
"""distributes an archive to your web servers"""
from fabric.api import put, run, env
from datetime import datetime
import os


env.user = "ubuntu"
env.hosts = ["3.95.32.122", "18.207.140.67"]


def deploy():
    """archive and deploy"""
    try:
        archive_path = do_pack()
    except Exception:
        return False
    return do_deploy(archive_path)


def do_pack():
    """ compress files and save to folder"""
    try:
        local("mkdir -p versions")
        path = ("versions/web_static_{}.tgz"
                .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
        check = local("tar -cvzf {} web_static".format(path), capture=True)
        return path
    except check.failed:
        return None


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
        return True
    except Exception:
        return False
