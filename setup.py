# Author - Arsharaj Chauhan
# This is the setup script for this python project.
# 
# Corona-Tracker-India  
# Copyright (C) 2020 Arsharaj Chauhan under GPL-v3


import setuptools

# reading long description from file 
with open('readme.md') as file: 
	long_description = file.read() 

# reading all the requirements
with open('requirements.txt') as file:
	required = file.read().splitlines()

# some more details 
classifiers = [ 
    'Development Status :: 4 - Beta',
    'Environment :: Console',
	'Intended Audience :: Healthcare Industry',
	'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: OS Independent',
	'Programming Language :: Python', 
	'Topic :: Internet', 
] 

# packages
my_packages = [
	'corona_tracker_india'
]

# calling the setup function 
setuptools.setup(
    name='corona-tracker-india', 
	version='0.1.0', 
	description='Corona disease tracker for India', 
	long_description=long_description, 
	long_description_content_type="text/markdown",
	url='https://github.com/arsharaj/corona-tracker-india',
	author='Arsharaj Chauhan', 
	author_email='arsharajchauhan343@gmail.com', 
	license='GPL', 
	packages=setuptools.find_packages(),
	classifiers=classifiers, 
	install_requires=required,
	python_requires='>=3.6',
	keywords='corona disease tracker for india'
) 
