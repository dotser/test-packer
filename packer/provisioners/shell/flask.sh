#!/usr/bin/env bash
set -eu


# Download Prana
# wget http://dl.bintray.com/netflixoss/Prana/Prana-0.0.1.zip
# unzip Prana-0.0.1.zip
# sudo mv Prana-0.0.1 /opt/Prana

echo '==> Installing pip requirements...'
sudo pip install flask
