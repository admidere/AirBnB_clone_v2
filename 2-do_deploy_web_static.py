#!/usr/bin/python3
""" A fabric script that generates a .tgz archive from the contents
    of the web_static folder and deploys it to web servers.
"""
from fabric.api import local, put, run, env
from datetime import datetime
import os


env.hosts = ['18.207.2.134', '100.25.152.180']


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = os.path.basename(archive_path)
        archive_name_no_ext = archive_name.split('.')[0]
        remote_path = "/data/web_static/releases/{}".format(archive_name_no_ext)

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/{}".format(archive_name))

        # Uncompress the archive to the folder on the web server
        run("mkdir -p {}".format(remote_path))
        run("tar -xzf /tmp/{} -C {}".format(archive_name, remote_path))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(archive_name))

        # Delete the symbolic link /data/web_static/current from the webserver
        run("rm -f /data/web_static/current")

        # Create a new symbolic link on the web server
        run("ln -s {} /data/web_static/current".format(remote_path))

        return True
    except Exception:
        return False
