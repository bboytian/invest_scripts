#!/bin/bash

wd=$(dirname $(realpath ${BASH_SOURCE[0]}))
logdir=/datastore_updater/cronlogs
logdate=/$(date '+%Y-%m-%d')
logfile=$wd$logdir$logdate.log

cd $wd

source ~/virtual_environments/invest_scripts/bin/activate

python -m datastore_updater #> $logfile 2>&1

deactivate
