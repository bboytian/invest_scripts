#!/bin/bash

realpath=/usr/local/bin/realpath
wd=$(dirname $(dirname $($realpath ${BASH_SOURCE[0]})))
env_dir=~/virtual_environments/invest_scripts

cd $wd
$env_dir/bin/python3 invest_scripts/eln_tracker/elnrec_clearer.py
