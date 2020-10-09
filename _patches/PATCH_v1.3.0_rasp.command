#!/bin/bash

wd=$(dirname $(realpath ${BASH_SOURCE[0]}))
cd $wd

echo -e '\n--- begin patch ---'

echo -e '\ninstalling packages'
env_dir=~/virtual_environments/invest_scripts
$env_dir/bin/pip3 install python-telegram-bot --upgrade

echo -e '\nconfiguring crontabs...'
crontab cronjobs.rasp

echo -e '\n--- patch complete ---'
