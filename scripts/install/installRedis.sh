#!/bin/bash
sudo apt -y install make gcc libc6-dev tcl
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
sudo make install
sudo src/redis-server > /var/log/redis &