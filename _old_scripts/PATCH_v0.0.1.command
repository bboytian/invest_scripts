#!/bin/bash

echo --- begin patch ---

echo -e '\nadding lines into ~/.bash_profile...'

app_str='\n
# ---------------\n
# PERSONNAL EDITS\n
\n
# anaconda3\n
. /opt/anaconda3/etc/profile.d/conda.sh'
echo -e "$app_str" >> ~/.bash_profile


echo -e '\nupdating crontab...'

wd=$(dirname $(realpath ${BASH_SOURCE[0]}))
runfile=$wd/RUN_DATASTORE_UPDATER.command
logdir=/datastore_updater/cronlogs
logdate='/$(date '+%Y-%m-%d')'
logfile=$wd$logdir$logdate.log
echo "00 18 * * * $runfile > $logfile 2>&1" > cronjobs.txt
yes | crontab $wd/cronjobs.txt


echo --- patch complete ---
