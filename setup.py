from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
	long_description = f.read()

setup(
	name='conda-autoenv',
	version='0.1',
	description='Automatic Conda Environment',
	long_description=long_description,
	url='https://github.com/sharonzhou/conda-autoenv',
	download_url='https://github.com/sharonzhou/conda-autoenv/tarball/0.1',
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
	keywords='conda auto env automatic environment directory entry pip requirements environment.yml yaml',
	packages=find_packages(),
	py_modules=["conda_autoenv"],
	install_requires=['conda'],
	scripts=['conda_autoenv.sh'],
)