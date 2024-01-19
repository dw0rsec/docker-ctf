#!/usr/bin/env python3

from datetime import datetime

import subprocess
import platform
import time
import sys
import os

class colors:
	PURPLE = '\033[95m'
	YELLOW = '\033[93m'
	GREEN = '\033[92m'
	BLUE = '\033[94m'
	RED = '\033[31m'
	STD = '\033[0m'

def runCommand(command, cwd=None):
	subprocess.call(command, cwd=cwd)

def checkRepos(repoUrl, directoryPath):
	repoName = repoUrl.split("/")[-1].replace(".git", "")
	repoPath = os.path.join(directoryPath, repoName)

	if os.path.exists(repoPath):
		currentTime = datetime.now()
		currentTime = currentTime.strftime('%H:%M:%S')
		print(f"[{colors.GREEN}*{colors.STD}]{colors.BLUE}{currentTime}{colors.STD} Repository already exists. Updating {repoName}...{colors.YELLOW}")
		runCommand(["git", "pull"], cwd=repoPath)
		print(f'{colors.STD}')
	else:
		currentTime = datetime.now()
		currentTime = currentTime.strftime('%H:%M:%S')
		print(f'[{colors.RED}!{colors.STD}]{colors.BLUE}{currentTime}{colors.STD} Repository not found. Cloning {repoName}...{colors.YELLOW}')
		runCommand(["git", "clone", repoUrl, repoPath])
		print(f'{colors.STD}')

def cloneRepos(repos, directoryPath):
	for repoUrl in repos:
		checkRepos(repoUrl, directoryPath)

def checkGroup(username):
	try:
		groupsOutput = subprocess.check_output(['groups', username])
		return 'docker' in groupsOutput.split()
	except subprocess.CalledProcessError as e:
		currentTime = datetime.now()
		currentTime = currentTime.strftime('%H:%M:%S')
		print(f'[{colors.RED}!{colors.STD}]{colors.BLUE}{currentTime}{colors.STD} Error checking groups for user {username}: {e}')
		return False

def printBanner():
	print(f'''
     █████                   █████
    ░░███                   ░░███
  ███████   ██████   ██████  ░███ █████  ██████  ████████
 ███░░███  ███░░███ ███░░███ ░███░░███  ███░░███░░███░░███
░███ ░███ ░███ ░███░███ ░░░  ░██████░  ░███████  ░███ ░░░
░███ ░███ ░███ ░███░███  ███ ░███░░███ ░███░░░   ░███
░░████████░░██████ ░░██████  ████ █████░░██████  █████
 ░░░░░░░░  ░░░░░░   ░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░
{colors.PURPLE}                       FOR HACKERS{colors.STD}

''')

def main():
	os.chdir(os.path.dirname(os.path.realpath(__file__)))
	directoryPath = "./"
	username = os.getenv('USER')
	namespace = 'user'
	imageName = 'docker-ctf'
	currentTime = datetime.now()
	currentTime = currentTime.strftime('%H:%M:%S')
	printBanner()

	if platform.system() != 'Linux':
		print(f'[{colors.RED}!{colors.STD}]{colors.BLUE}{currentTime}{colors.STD} This Program only runs on Linux hosts...')
		print('')
		time.sleep(1)
		sys.exit()
	else:
		print(f"[{colors.YELLOW}i{colors.STD}]{colors.BLUE}{currentTime}{colors.STD} Build will take around 15-20 mins.")
		print(f"[{colors.YELLOW}i{colors.STD}]{colors.BLUE}{currentTime}{colors.STD} Checking for necessary repos...")
		time.sleep(1)

	repos = [
		'https://github.com/rapid7/metasploit-framework.git',
		'https://gitlab.com/exploit-database/exploitdb.git',
		'https://github.com/OJ/gobuster.git',
		'https://github.com/danielmiessler/SecLists.git',
		'https://github.com/Gallopsled/pwntools.git',
		'https://github.com/radareorg/radare2.git',
		'https://github.com/sqlmapproject/sqlmap.git',
		'https://github.com/wpscanteam/wpscan.git',
		'https://github.com/openwall/john.git',
		'https://github.com/longld/peda.git',
		'https://github.com/rbenv/ruby-build.git'
	]

	cloneRepos(repos, directoryPath)

	if checkGroup(username):
		dockerBuild = [
			'docker',
			'build',
			'-t', '{}/{}'.format(namespace, imageName),
			'.'
		]
	else:
		dockerBuild = [
			'sudo', '-g', 'docker',
			'docker',
			'build',
			'-t', '{}/{}'.format(namespace, imageName),
			'.'
		]

	currentTime = datetime.now()
	currentTime = currentTime.strftime('%H:%M:%S')
	print(f"[{colors.YELLOW}i{colors.STD}]{colors.BLUE}{currentTime}{colors.STD} Building the Docker image...")
	subprocess.call(dockerBuild)
	currentTime = datetime.now()
	currentTime = currentTime.strftime('%H:%M:%S')
	print(f"[{colors.YELLOW}i{colors.STD}]{colors.BLUE}{currentTime}{colors.STD} Build complete. Run instantiate.py to start.")

if __name__ == '__main__':
	main()
