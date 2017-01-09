=======================
**Conda-autoenv: Environments by Directory for Conda**
=======================

Automatically activate, update, and deactivate conda environments from an environment.yml file in a directory. 

If a pip requirements.txt file exists as well, that will also be installed in the environment and updated upon deactivation.


Install
----

::

    $ pip install conda-autoenv
    $ echo "source `which conda_autoenv.sh`" >> ~/.bash_profile


Usage
----

Existing environment.yml file, with or without conda environment
~~~~~~~~~~~~~~~~~~~~~~~

If you already have an environment.yml file, place that in your directory (along with your pip requirements.txt file, if applicable), and conda-autoenv will automatically activate that environment and if applicable, create it beforehand. 

No environment.yml file, with a conda environment
~~~~~~~~~~~~~~~~~~~~~~~

If you do not have an environment.yml file, but have a conda environment, export your conda environment to an environment.yml file by executing (in the environment's root directory, while your environment is activated):

::

	$ conda env export > environment.yml

*[Optional]* You may also want your pip packages to automatically be activated and updated with your environment. If so, execute:

::

	$ pip freeze > requirements.txt

No conda environment or environment.yml file (yet!)
~~~~~~~~~~~~~~~~~~~~~~~

If you do not have a conda environment, create one by executing (replace ENV_NAME with the name you would like to call your environment):

::
	
	$ conda create -n ENV_NAME

Then, activate your environment by executing (replace ENV_NAME with the name you gave your environment):

::

	$ source activate ENV_NAME

Finally, export your environment to an environment.yml file to be automatically activated later:

::

	$ conda env export > environment.yml

*[Optional]* You may also want your pip packages to automatically be activated and updated with your environment. If so, execute:

::

	$ pip freeze > requirements.txt

