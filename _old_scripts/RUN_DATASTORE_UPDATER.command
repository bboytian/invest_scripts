#!/bin/bash

realpath=/usr/local/bin/realpath
wd=$(dirname $($realpath ${BASH_SOURCE[0]}))
cd $wd

eval "$(conda shell.bash hook)"
conda deactivate
conda activate invest_scripts

python -m datastore_updater

conda deactivate
