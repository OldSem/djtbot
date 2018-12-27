#!/usr/bin/env bash
echo "update"
sudo apt-get update

echo "install requirements"
sudo apt-get install -y build-essential
sudo apt-get install -y checkinstall
sudo apt-get install -y libreadline-gplv2-dev
sudo apt-get install -y libncursesw5-dev
sudo apt-get install -y libssl-dev
sudo apt-get install -y libsqlite3-dev
sudo apt-get install -y tk-dev
sudo apt-get install -y libgdbm-dev
sudo apt-get install -y libc6-dev
sudo apt-get install -y libbz2-dev
sudo apt-get install -y zlib1g-dev
sudo apt-get install -y openssl
sudo apt-get install -y libffi-dev
sudo apt-get install -y python3-dev
sudo apt-get install -y python3-setuptools
sudo apt-get install -y wget
sudo apt-get install -y python3-pip
sudo apt-get install -y supervisor
sudo apt-get install -y nginx
sudo apt-get install -y postgresql
sudo apt-get install -y postgresql-contrib
sudo apt-get install -y curl
sudo apt-get install -y virtualenv

echo "Prepare to build"
mkdir /tmp/Python37
cd /tmp/Python37

echo "Pull down Python 3.7, build, and install"
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
tar xvf Python-3.7.0.tar.xz
cd /tmp/Python37/Python-3.7.0
./configure
sudo make altinstall

echo "enable postgres"
sudo systemctl enable postgresql@10-main.service