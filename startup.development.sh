#!/usr/bin/env bash
# ##############################################################################
# Starting script project folder.
# Creates configs directory and related environmental variables for accessing
# local database and running python virtualenv.
#
# Dependencies:
#   - mysql-client, virtualenv, python3.6
#
# Other env vars (optional):
#
# ##############################################################################

cd "$(dirname "$0")" || exit 1
WD="$(pwd)"

# [CMD Arguments and Env. Vars]

venvdir="$(pwd)/inventorytracker"
pipfile="requirements.txt"


echo -e "Installing venv to $venvdir \
    \nInstalling packages from '$WD/$pipfile'"


if [ "$(uname -s)" == "Linux" ]; then
    macos=false
elif [ "$(uname -s)" == "Darwin" ]; then
    macos=true
else
    echo -e "\n[error] Could not determine os. Assuming Windows. Quitting\n"
    exit 1
fi
echo "MacOS operating system: $macos"


# [Environment setup]
# if configs/ exists, prompt to rebuild or pass.
# Else if configs/ D.N.E. then ask for MySQL user credentials and
# build environmental vars.
if [ -d "${WD}/configs" ];
then
    echo -e "Rebuild local project directory and update sql configurations? \n"
    echo -n "[y/n] "
    read response

    first=${response:0:1}
    first=$(echo "$first" | tr '[:upper:]' '[:lower:]')
    if [ "${first}" == "n" ]; then
        rebuild=false
    fi
else
    mkdir ${WD}/configs
fi

rebuild=${rebuild:=true}


# Build python virtualenv environment using pip and requirements file.

# Check if virtualenv is installed on the system
if [ -z "$(which virtualenv)" ]; then
    echo -e "python virtualenv command not found."
    echo -e "\nYou need virtualenv to continue with the setup. \
        \nMacOS users can install with pip: \t\tpip install virtualenv \
        \nLinux users should use apt: \t\tapt install virtualenv \
        \nPlease install then run this setup again."
fi

if [ ! -d "${venvdir}/venv" ]; then
	virtualenv -p python3 ${venvdir}/venv
    if [ $? -ne 0 ]; then
    	echo -e "\n[error] could not install python dependencies. \
            \nPlease check that virtualenv is installed and on your PATH."
        exit 1
    fi
    echo -e "\nsource ${WD}/configs/.env" >> ${venvdir}/venv/bin/activate
fi

source ${venvdir}/venv/bin/activate
${venvdir}/venv/bin/pip install -r $WD/$pipfile



echo -e "Install complete!"

