#!/usr/bin/env python3

import subprocess

namespace = 'user'
imagename = 'docker-ctf'

docker_run = [
	'sudo', '-g', 'docker',
	'docker',
	'run',
	'--network', 'host',
	'-it', '{}/{}'.format(namespace, imageName)
]

subprocess.call(docker_run)
