#!/usr/bin/python3
""" A fabric script that generates a .tgz archive from the contents
    of the web_static folder and deploys it to web servers.
"""


import os
from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['18.207.2.134', '100.25.152.180']


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False

    archive_name = os.path.basename(archive_path)
    archive_dir = os.path.splitext(archive_name)[0]

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Uncompress the archive to the folder
        # /data/web_static/releases/<archive filename without extension>
        # on the web server
        run("mkdir -p /data/web_static/releases/{}/".format(archive_dir))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive_name, archive_dir))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(archive_name))

        # Move the contents of the web static directory tothe parent directory
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(archive_dir, archive_dir))

        # Remove the web static directory
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(archive_dir))

        # Delete the symbolic link /data/web_static/current from the webserver
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current on the webserver
        # linked to the new version of your code (/data/web_static/releas
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(archive_dir))

        print("New version deployed!")
        return True

    except Exception:
        return False
