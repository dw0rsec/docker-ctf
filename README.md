![banner.png](banner.png "banner.png")

### About docker-ctf

docker-ctf is a Docker container that can be used as a lean VM replacement for hacking. It should be noted that, unlike VMs, the container runs on the kernel of the host system and is only isolated by namespaces and cgroups. docker-ctf is based on a Debian image and has the following tools installed:

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


To get started, simply run build.py (the build can take up to 15-20 minutes, depending on the internet connection and hardware used) and start the container after the build with instantiate.py.
