#!/bin/bash

wd=$(dirname $(realpath ${BASH_SOURCE[0]}))
cd $wd

echo -e '\n--- begin patch ---'

echo -e '\nconfiguring crontabs...'
echo "wd=$wd" | cat - cronjobs.txt > temp && mv temp cronjobs.txt
crontab cronjobs.txt

echo -e '\n--- patch complete ---'
