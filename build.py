#!/usr/bin/env python3

from datetime import datetime

import subprocess
import platform
import time
import sys
import os

class Colors:
	PURPLE = '\033[95m'
	YELLOW = '\033[93m'
	GREEN = '\033[92m'
	BLUE = '\033[94m'
	RED = '\033[31m'
	STD = '\033[0m'

def run_command(command, cwd=None):
	subprocess.call(command, cwd=cwd)

def check_repos(repo_url, directory_path):
	repo_name = repo_url.split("/")[-1].replace(".git", "")
	repo_path = os.path.join(directory_path, repo_name)

	if os.path.exists(repo_path):
		current_time = datetime.now()
		current_time = current_time.strftime('%H:%M:%S')
		print(f"[{Colors.GREEN}*{Colors.STD}]{Colors.BLUE}{current_time}{Colors.STD} Repository already exists. Updating {repo_name}...{Colors.YELLOW}")
		run_command(["git", "pull"], cwd=repo_path)
		print(f'{Colors.STD}')
	else:
		current_time = datetime.now()
		current_time = current_time.strftime('%H:%M:%S')
		print(f'[{Colors.RED}!{Colors.STD}]{Colors.BLUE}{current_time}{Colors.STD} Repository not found. Cloning {repo_name}...{Colors.YELLOW}')
		run_command(["git", "clone", repo_url, repo_path])
		print(f'{Colors.STD}')

def clone_repos(repos, directory_path):
	for repo_url in repos:
		check_repos(repo_url, directory_path)

def check_group(username):
	try:
		groups_output = subprocess.check_output(['groups', username])
		return 'docker' in groups_output.split()
	except subprocess.CalledProcessError as e:
		current_time = datetime.now()
		current_time = current_time.strftime('%H:%M:%S')
		print(f'[{Colors.RED}!{Colors.STD}]{Colors.BLUE}{current_time}{Colors.STD} Error checking groups for user {username}: {e}')
		return False

def print_banner():
	print(f'''
     █████                   █████
    ░░███                   ░░███
  ███████   ██████   ██████  ░███ █████  ██████  ████████
 ███░░███  ███░░███ ███░░███ ░███░░███  ███░░███░░███░░███
░███ ░███ ░███ ░███░███ ░░░  ░██████░  ░███████  ░███ ░░░
░███ ░███ ░███ ░███░███  ███ ░███░░███ ░███░░░   ░███
░░████████░░██████ ░░██████  ████ █████░░██████  █████
 ░░░░░░░░  ░░░░░░   ░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░
{Colors.PURPLE}                       FOR HACKERS{Colors.STD}

''')

def main():
	os.chdir(os.path.dirname(os.path.realpath(__file__)))
	directory_path = "./"
	username = os.getenv('USER')
	namespace = 'user'
	imagename = 'docker-ctf'
	current_time = datetime.now()
	current_time = current_time.strftime('%H:%M:%S')
	print_banner()

	if platform.system() != 'Linux':
		print(f'[{Colors.RED}!{Colors.STD}]{Colors.BLUE}{current_time}{Colors.STD} This Program only runs on Linux hosts...')
		print('')
		time.sleep(1)
		sys.exit()
	else:
		print(f"[{Colors.YELLOW}i{Colors.STD}]{Colors.BLUE}{current_time}{Colors.STD} Build will take around 15-20 mins.")
		print(f"[{Colors.YELLOW}i{Colors.STD}]{Colors.BLUE}{current_time}{Colors.STD} Checking for necessary repos...")
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

	clone_repos(repos, directory_path)

	if check_group(username):
		docker_build = [
			'docker',
			'build',
			'-t', '{}/{}'.format(namespace, imagename),
			'.'
		]
	else:
		docker_build = [
			'sudo', '-g', 'docker',
			'docker',
			'build',
			'-t', '{}/{}'.format(namespace, imagename),
			'.'
		]

	current_time = datetime.now()
	current_time = current_time.strftime('%H:%M:%S')
	print(f"[{Colors.YELLOW}i{Colors.STD}]{Colors.BLUE}{current_time}{Colors.STD} Building the Docker image...")
	subprocess.call(docker_build)
	current_time = datetime.now()
	current_time = current_time.strftime('%H:%M:%S')
	print(f"[{Colors.YELLOW}i{Colors.STD}]{Colors.BLUE}{current_time}{Colors.STD} Build complete. Run instantiate.py to start.")

if __name__ == '__main__':
	main()
