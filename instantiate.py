#!/usr/bin/env python3

import subprocess

namespace = 'user'
imageName = 'docker-ctf'

dockerRun = [
	'sudo', '-g', 'docker',
	'docker',
	'run',
	'--network', 'host',
	'-it', '{}/{}'.format(namespace, imageName)
]

subprocess.call(dockerRun)
