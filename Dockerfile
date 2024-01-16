FROM debian:latest

ENV TERM=xterm-256color

RUN \
	apt-get update && apt-get install -y \
		bash-completion \
		gdb \
		vim \
		tmux \
		nmap \
		ssh \
		tcpdump \
		netcat-openbsd \
		curl \
		net-tools \
		wget \
		python3 \
		python3-pip \
		python3-dev \
		libffi-dev \
		git \
		autoconf \
		build-essential \
		libpcap-dev \
		libpq-dev \
		zlib1g-dev \
		libsqlite3-dev \
		libssl-dev \
		yasm \
		pkg-config \
		libgmp-dev \
		libpcap-dev \
		libbz2-dev

RUN \
	groupadd --gid 1337 user && \
	useradd -m --uid 1337 --gid 1337 user && \
	chmod 700 ~user && \
	mkdir ~user/opt && chown user:user ~user/opt

COPY metasploit-framework /home/user/opt/metasploit-framework
COPY exploitdb /home/user/opt/exploitdb
COPY gobuster /home/user/opt/gobuster
COPY SecLists /home/user/opt/SecLists
COPY pwntools /home/user/opt/pwntools
COPY radare2 /home/user/opt/radare2
COPY sqlmap /home/user/opt/sqlmap
COPY wpscan /home/user/opt/wpscan
COPY john /home/user/opt/john
COPY peda /home/user/opt/peda
COPY .bashrc /home/user/.bashrc

RUN \
	chown --recursive user:user ~user/opt/metasploit-framework && \
	chown --recursive user:user ~user/opt/exploitdb && \
	chown --recursive user:user ~user/opt/gobuster && \
	chown --recursive user:user ~user/opt/SecLists && \
	chown --recursive user:user ~user/opt/pwntools && \
	chown --recursive user:user ~user/opt/radare2 && \
	chown --recursive user:user ~user/opt/sqlmap && \
	chown --recursive user:user ~user/opt/wpscan && \
	chown --recursive user:user ~user/opt/john && \
	chown --recursive user:user ~user/opt/peda && \
	chown user:user ~user/.bashrc

USER user

WORKDIR /home/user/opt/john/src/
RUN ./configure && make -s clean && make -sj12

RUN \
	git clone https://github.com/rbenv/rbenv.git ~/.rbenv && \
	echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc && \
	echo 'eval "$(~/.rbenv/bin/rbenv init -)"' >> ~/.bashrc && \
	mkdir ~/.rbenv/plugins

USER root

COPY ruby-build /home/user/.rbenv/plugins/ruby-build
RUN \
	chown --recursive user:user ~user/.rbenv/plugins/ruby-build && \
	wget https://go.dev/dl/go1.21.6.linux-amd64.tar.gz && \
	tar -C /usr/local -xzf go1.21.6.linux-amd64.tar.gz && \
	rm -rv go1.21.6.linux-amd64.tar.gz && \
	/home/user/opt/radare2/sys/install.sh
	
USER user

RUN \
	export PATH="$HOME/.rbenv/bin:$PATH" && \
	rbenv install $(cat ~/opt/metasploit-framework/.ruby-version) && \
	rbenv install $(cat ~/opt/wpscan/.ruby-version)

RUN \
	bash -i -c '. ~/.bashrc && \
	rbenv shell $(cat ~/opt/metasploit-framework/.ruby-version) && \
	gem install bundler && \
	bundle install --gemfile=~/opt/metasploit-framework/Gemfile && \
	rbenv shell $(cat ~/opt/wpscan/.ruby-version) && \
	gem install wpscan'

WORKDIR /home/user/opt/gobuster

RUN \
	pip install --upgrade --editable /home/user/opt/pwntools --break-system-packages && \
	export PATH=$PATH:/usr/local/go/bin && \
	wget -P /home/dw0rsec/ https://raw.githubusercontent.com/dw0rsec/dotfiles/main/.vimrc && \
	echo "source /home/user/opt/peda/peda.py" >> ~/.gdbinit && \
	echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc && \
	export PATH=$PATH:/usr/local/go/bin && \
	go get && go build

WORKDIR /home/user
ENTRYPOINT ["bash"]
