#!/usr/bin/python3
"""Write a Fabricscript that generates a .tgz archive from
the contents of the web_static folder of your AirBnB Clone repo
using the function do_pack."""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    # Create the versions folder if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Generate the archive name with the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)
    # Create the .tgz archive and capture the output
    result = local("tar -cvzf versions/{} web_static".format(archive_name))

    # Return the archive path if the archive was created successfully
    # otherwise return None
    if result.failed:
        return None
    return os.path.join("versions", result)
