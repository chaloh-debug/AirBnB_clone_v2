#!/usr/bin/python3
"""distributes an archive to your web servers"""
from fabric.api import *
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
        local("tar -cvzf {} web_static".format(path))
        return path
    except Exception:
        return None


def do_deploy(archive_path):
    """deploy to server"""
    if not exists(archive_path):
        return False
    try:
        filename = archive_path.split("/")[-1].split(".")[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(filename))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(filename, filename))
        run('rm -rf /tmp/{}.tgz'.format(filename))
        run(('mv /data/web_static/releases/{}/web_static/* ' +
            '/data/web_static/releases/{}/')
            .format(filename, filename))
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(filename))
        run('rm -rf /data/web_static/current')
        run(('ln -s /data/web_static/releases/{}/' +
            ' /data/web_static/current')
            .format(filename))
        print("Successfully deployed!!")
        return True
    except Exception:
        return False
