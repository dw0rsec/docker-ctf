![banner.png](banner.png "banner.png")

## About docker-ctf

`docker-ctf` is a Docker container that can be used as a lean VM replacement for hacking. It should be noted that, unlike VMs, the container runs on the kernel of the host system and is only isolated by namespaces and cgroups. This Docker container provides a Debian-based environment pre-configured with essential tools for penetration testing and ethical hacking.

## Features

- Debian base image for stability and reliability

- Pre-installed penetration testing tools, including:

	- [Metasploit](https://github.com/rapid7/metasploit-framework)

	- [SearchSploit](https://gitlab.com/exploit-database/exploitdb)

	- [gobuster](https://github.com/OJ/gobuster)

	- [John the Ripper](https://github.com/openwall/john)

	- [peda](https://github.com/longld/peda)

	- [pwntools](https://github.com/Gallopsled/pwntools)

	- [radare2](https://github.com/radareorg/radare2)

	- [SecLists](https://github.com/danielmiessler/SecLists)

	- [sqlmap](https://github.com/sqlmapproject/sqlmap)

	- [WPScan](https://github.com/wpscanteam/wpscan)

- Lightweight (compared to a VM) and optimized for rapid deployment

- Easily customizable for additional tools or personal preferences

## Prerequisites

Before using `docker-ctf`, ensure that the following prerequisites are met:

1. **Docker Environment**: You need to have Docker installed on your host system. If you don't have Docker installed, you can download and install it from the official [Docker website](https://www.docker.com/get-started).

2. **Git**: Make sure Git is installed on your system. If Git is not installed, you can download it from the official [Git website](https://git-scm.com/downloads).

3. **Python 3**: The build and instantiation scripts are written in Python 3. Make sure you have Python 3 installed on your system. You can download Python from the official [Python website](https://www.python.org/downloads/).

These prerequisites are essential for building and running the `docker-ctf` container on your machine.

## Usage

>:warning: Note: The build.py script was only written for Linux, but should also run on macOS systems with a few adjustments.

1. Build the Docker image (the build can take up to 15-20 minutes)

```shell
python3 build.py
```

2. Run the container

```shell
python3 instantiate.py
```

3. Start using your favorite penetration testing tools!

## Customization

Feel free to customize the Dockerfile to include additional tools or configurations according to your specific needs.
