#!/bin/bash


# Checking with user
prereq_declare='\n
to proceed with installation, ensure that you have installed the following pre-requisites: \n
\t -> homebrew install coreutils; if running mac, for "realpath"\n
\t -> virtualenv installed, sudo pip3 for mac, pip3 for rasp\n
\t -> google chrome browser \n
\n
,if not, please close the terminal and install the programs before proceeding.\n
'
echo -e $prereq_declare
read -r -p "Do you have the pre-requisites? y or n " response   


echo -e '\n--- begin patch ---'
if [[ $response =~ ^([yY][eE][sS]|[yY])$ ]]
then

    echo -e '\ncreating virtual environment...'
    wd=$(dirname $(realpath ${BASH_SOURCE[0]}))    
    env_dir=~/virtual_environments/invest_scripts
    mkdir -p $env_dir
    virtualenv $env_dir -p python3


    echo -e '\ninstalling python dependencies...'
    cd $wd
    $env_dir/bin/python3 setup.py develop


    echo -e '\n--- patch complete ---'


else
    echo -e '\n--- patch cancelled ---'
    exit 0

fi
