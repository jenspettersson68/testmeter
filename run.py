#!/usr/bin/env python3
# -*- encoding: utf8 -*-
"""docker_run_bash.py

Example of how to run a shell script inside of a docker container.
"""

from subprocess import call
import docker
import os
import sys
import tempfile

# Get the text editor from the shell, otherwise default to Vim
EDITOR = os.environ.get('EDITOR','vim')

# Select which docker container to use (default to busybox-bash)
container = sys.argv[1] if len(sys.argv)>=2 else "blang/busybox-bash"

# Instantiate a Docker client object
client = docker.from_env(assert_hostname=False)

# Create a temporary directory
with tempfile.TemporaryDirectory(dir="/tmp") as td:

    # Create a temporary file in that directory
    tf = tempfile.NamedTemporaryFile(dir=td, delete=False)

    # Write to the temporary file
    tf.write("# Enter command to execute...".encode())

    # Flush the I/O buffer to make sure the data is written to the file
    tf.flush()

    # Open the file with the text editor
    call([EDITOR, tf.name])

    # Get the path to the mounted file on the container
    mounted_file = os.path.join("/mnt/host", os.path.basename(tf.name))

    # Execute the script
    cmd_stdout = client.containers.run(
        container,
        "/bin/bash {}".format(mounted_file),
        remove=True,
        volumes={
            td: {
                'bind': '/mnt/host',
                'mode': 'ro',
            }
        }
    )

    # Delete the file
    os.unlink(tf.name)

    # Output the results
    print("Command output:\n{}".format(cmd_stdout.decode()))#!/usr/bin/env python3
# -*- encoding: utf8 -*-
"""docker_run_bash.py

Example of how to run a shell script inside of a docker container.
"""

from subprocess import call
import docker
import os
import sys
import tempfile

# Get the text editor from the shell, otherwise default to Vim
EDITOR = os.environ.get('EDITOR','nano')

# Select which docker container to use (default to busybox-bash)
container = sys.argv[1] if len(sys.argv)>=2 else "mesmeratu/todo:latest"

# Instantiate a Docker client object
client = docker.from_env(assert_hostname=False)

# Create a temporary directory
with tempfile.TemporaryDirectory(dir="/tmp") as td:

    # Create a temporary file in that directory
    tf = tempfile.NamedTemporaryFile(dir=td, delete=False)

    # Write to the temporary file
    tf.write("# Enter command to execute...".encode())

    # Flush the I/O buffer to make sure the data is written to the file
    tf.flush()

    # Open the file with the text editor
    call([EDITOR, tf.name])

    # Get the path to the mounted file on the container
    mounted_file = os.path.join("/mnt/host", os.path.basename(tf.name))

    # Execute the script
    cmd_stdout = client.containers.run(
        container,
        "/bin/bash {}".format(mounted_file),
        remove=True,
        volumes={
            td: {
                'bind': '/mnt/host',
                'mode': 'ro',
            }
        }
    )

    # Delete the file
    os.unlink(tf.name)

    # Output the results
    print("Command output:\n{}".format(cmd_stdout.decode()))
