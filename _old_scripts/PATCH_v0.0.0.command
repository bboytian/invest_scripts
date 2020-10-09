#!/bin/bash


# Checking with user
prereq_declare='\n
to proceed with installation, ensure that you have installed the following pre-requisites: \n
\t -> home-brew; with coreutils installed \n
\t -> anaconda mini \n
\t -> google chrome browser, version 79 \n
\n
,if not, please close the terminal and install the programs before proceeding.\n
'
echo -e $prereq_declare
read -r -p "Do you have the pre-requisites? y or n " response   


echo -e '\n--- begin patch ---'
if [[ $response =~ ^([yY][eE][sS]|[yY])$ ]]
then

    echo -e '\ncreating conda environment...'
    eval "$(conda shell.bash hook)" # enables us to interact with conda via shell script
    conda deactivate
    yes | conda install conda
    yes | conda create -n invest_scripts python=3.7


    echo -e '\ninstalling python dependencies...'
    cd -- "$(dirname "$BASH_SOURCE")"
    conda activate invest_scripts
    python setup.py develop
    conda deactivate


    echo -e '\n--- patch complete ---'


else
    echo -e '\n--- patch cancelled ---'
    exit 0

fi
