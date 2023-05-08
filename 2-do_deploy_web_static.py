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

   file_name = os.path.basename(archive_path)
   archive_name = os.path.splitext(file_name)[0]

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Create the directory to uncompress the archive
        run('mkdir -p /data/web_static/releases/{}/'.format(archive_name))

        # Uncompress the archive to the folder
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(file_name, archive_name))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(file_name))

        # Move the files to the new folder and remove the old folder
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(archive_name,
                                                  archive_name))
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(archive_name))

        # Delete the symbolic link /data/web_static/current from the web
        run('rm -rf /data/web_static/current')

        # Create a new the symbolic link /data/web_static/current
        run('ln -s /data/web_static/releases/{}/ \
            /data/web_static/current'.format(archive_name))

        print('New version deployed!')
        return True

    except Exception:
        return False
