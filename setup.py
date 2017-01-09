from setuptools import setup, find_packages

long_description='Automatically activate, update, and deactivate conda environments from an environment.yml file in a directory.\n\nIf a pip requirements.txt file exists as well, that will also be installed in the environment and updated upon deactivation.'

setup(
	name='conda-autoenv',
	version='0.2',
	description='Environments by Directory for Conda',
	long_description=long_description,
	url='https://github.com/sharonzhou/conda-autoenv',
	download_url='https://github.com/sharonzhou/conda-autoenv/tarball/0.2',
	author='Sharon Zhou',
	author_email='sharonzpost@gmail.com',
	license='MIT',
	classifiers=[
		'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
	],
	keywords=['conda', 'auto', 'env', 'automatic', 'environment', 'directory', 'pip requirements', 'environment.yml', 'yaml'],
	packages=find_packages(),
	install_requires=['conda'],
	scripts=['conda_autoenv.sh']
)