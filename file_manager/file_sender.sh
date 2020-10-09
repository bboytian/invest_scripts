#!/bin/bash

# This script acts as a file sender to the tian-home-rasp3bp located at home.
# The router at home is port forwarded to the raspberry pi on the local network

# First time user set up would require adding of ECDSA key fingerprint
# thus the script cannot be run yet
source host_secret.sh

realpath=/usr/local/bin/realpath

server_dir=/home/$user/projects/invest_scripts_repo/inbox
client_dir=$(dirname $(dirname $(dirname $($realpath ${BASH_SOURCE[0]}))))

echo $client_dir

server_file=datastore_$(date "+%Y%m%d").xlsx
client_file=datastore.xlsx

echo -e '\n---Performing file transfers...---'

echo -e "\ntransferring $client_file..."
scp -v -P $port $client_dir/$client_file $user@$dns:$server_dir/$server_file

echo -e "\n---file transfer complete!---"
