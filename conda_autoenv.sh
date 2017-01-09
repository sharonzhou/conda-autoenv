#!/bin/bash

# conda-autoenv automatically 
#  (1) activates a conda environment per the environment.yml file in 
#      a directory, when you enter it
#  (2) updates the file and deactivates the environment, when you
#      leave the directory
#  (3) installs and updates your pip requirements per the 
#      requirements.txt in the directory as well
# 
# To install, add this line to your .bashrc or .bash-profile:
#
#       source /path/to/conda_autoenv.sh
#

function conda_autoenv() {
  if [ -e "environment.yml" ]; then
    ENV=$(head -n 1 environment.yml | cut -f2 -d ' ')
    # Check if you are already in the environment
    if [[ $PATH != *$ENV* ]]; then
      # Check if the environment exists
      if source activate $ENV && [[ $? -eq 0 ]]; then
        # Set root directory of active environment
        CONDA_ENV_ROOT="$(pwd)"
      else
        echo "Creating conda environment '$ENV' from environment.yml ('$ENV' was not found using 'conda env list')"
        conda env create -q -f environment.yml
        echo "'$ENV' successfully created and will automatically activate in this directory"
        source activate $ENV
        if [ -e "requirements.txt" ]; then
          echo "Installing pip requirements from requirements.txt"
          pip install -q -r requirements.txt
          echo "Pip requirements successfully installed"
        fi
      fi
    fi
  elif [[ $PATH = */envs/* ]]\
    && [[ $(pwd) != $CONDA_ENV_ROOT ]]\
    && [[ $(pwd) != $CONDA_ENV_ROOT/* ]]
  then
    echo "Deactivating conda environment"
    export PIP_FORMAT=columns
    echo "Updating conda environment.yml (and pip requirements.txt)"
    conda env export > $CONDA_ENV_ROOT/environment.yml
    pip freeze > $CONDA_ENV_ROOT/requirements.txt
    CONDA_ENV_ROOT=""
    echo "Successfully updated environment.yml and requirements.txt"
    source deactivate
    echo "Deactivated successfully"
  fi
}

export PROMPT_COMMAND=conda_autoenv