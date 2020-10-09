#!/bin/bash

wd=$(dirname $(realpath ${BASH_SOURCE[0]}))    
env_dir=~/virtual_environments/invest_scripts

$env_dir/bin/python3 $wd/file_receiver.py
