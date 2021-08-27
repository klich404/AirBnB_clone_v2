#!/usr/bin/python3
"""
creates and distributes an archive to your
web servers, using the function deploy
"""

from fabric.api import *
import time
import os.path
env.hosts = ['35.237.143.111', '34.227.206.85']


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    date = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".format(date))
        return("versions/web_static_{}.tgz".format(date))
    except:
        return None


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if (os.path.isfile(archive_path) is False):
        return False
    path_split = archive_path.split("/")[-1]
    path_com = ("/data/web_static/releases/" + path_split.split(".")[0])
    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(path_com))
        run("sudo tar -xzf /tmp/{} -C {}".format(path_split, path_com))
        run("sudo rm /tmp/{}".format(path_split))
        run("sudo mv {}/web_static/* {}/".format(path_com, path_com))
        run("sudo rm -rf {}/web_static".format(path_com))
        run("sudo rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path_com))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to your web servers"""
    try:
        archive = do_pack()
        result = do_deploy(archive)
        return result
    except:
        return False
