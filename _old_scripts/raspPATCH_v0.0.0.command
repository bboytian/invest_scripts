#!/bin/bash


# Checking with user
prereq_declare='\n
to proceed with installation, ensure that you have installed the following pre-requisites: \n
\t -> virtualenv installed\n
\t -> google chrome browser \n
\n
,if not, please close the terminal and install the programs before proceeding.\n
'
echo -e $prereq_declare
read -r -p "Do you have the pre-requisites? y or n " response   



if [[ $response =~ ^([yY][eE][sS]|[yY])$ ]]
then

    echo -e '\n--- begin patch ---'
    
    echo -e '\ncreating virtual environment...'
    virtualenv=~/.local/bin/virtualenv # THIS LINE FOR RASP
    env_dir=~/virtual_environments/invest_scripts
    $virtualenv $env_dir


    echo -e '\ninstalling python dependencies...'
    cd -- "$(dirname "$BASH_SOURCE")"
    source $env_dir/bin/activate
    python3 setup.py develop
    deactivate


    echo -e '\n--- patch complete ---'


else
    echo -e '\n--- patch cancelled ---'
    exit 0

fi
