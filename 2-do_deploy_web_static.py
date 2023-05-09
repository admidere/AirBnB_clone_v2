#!/usr/bin/python3
""" A fabric script that generates a .tgz archive from the contents
    of the web_static folder and deploys it to web servers.
"""


from fabric.api import env, put, run
from os.path import exists

env.user = 'ubuntu'
env.hosts = ['18.207.2.134', '100.25.152.180']
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    if not exists(archive_path):
        return False

     # Get the archive name without its extension (.tgz)
    archive_name = archive_path.split("/")[-1]
    archive_name_no_extension = archive_name.split(".")[0]
    # Uncompress the archive to
    # /data/web_static/releases/archive_name_no_extension
    destined_folder = "/data/web_static/releases/{}/"\
                      .format(archive_name_no_extension)

    # Returns True if all operations have been done correctly,
    # otherwise returns False
    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        # Create a directory where it should be uncompressed
        run("mkdir -p {}".format(destined_folder))
        # Uncompress to the destined directory
        run("tar -xzf /tmp/{} -C {}".format(archive_name, destined_folder))
        # Delete the uploded archive (in /tmp/ directory)
        run("rm /tmp/{}".format(archive_name))
        # Move all files inside web_static to the destined_folder created
        run("mv {}web_static/* {}".format(destined_folder, destined_folder))
        # Delte the empty web_static folder
        run("rm -rf {}web_static".format(destined_folder))
        # Delete the symbolic link
        run("rm -rf /data/web_static/current")
        # Create a new symbolic link
        run("ln -s {} /data/web_static/current".format(destined_folder))
        print("New version deployed!")
        return True
    except:
        return False
