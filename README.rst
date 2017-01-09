
*conda-autoenv*

=======================

Automatically activate, update, and deactivate conda environments from an environment.yml file in a directory. If pip a requirements.txt file also exists, that will also be installed in the environment and be updated.

----

*Usage*

Add the following line to your ~/.bashrc or ~/.bash_profile:

	source ~/conda_autoenv.sh

Case 0. If you already have an environment.yml file, place that in your directory (along with your pip requirements.txt file, if applicable), and conda-autoenv will automatically activate that environment. 

Case 1. If you do not have an environment.yml file, but have a conda environment, export your conda environment to an environment.yml file by executing (in the environment's root directory, while your environment is activated):

	conda env export > environment.yml

Case 2. If you do not have a conda environment, create one by executing (replace ENV_NAME with the name you would like to call your environment):

	conda create -n ENV_NAME

Then, activate your environment by executing (replace ENV_NAME with the name you gave your environment):
	
	source activate ENV_NAME

Finally, export your environment to an environment.yml file to be automatically activated later:

	conda env export > environment.yml