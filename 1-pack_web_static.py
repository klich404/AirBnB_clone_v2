#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack
"""

from fabric.api import *
import time


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    date = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".format(date))
        return("versions/web_static_{}.tgz".format(date))
    except:
        return None
