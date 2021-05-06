# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in expensify_integration/__init__.py
from expensify_integration import __version__ as version

setup(
	name='expensify_integration',
	version=version,
	description='Integrate Expensify to ERPNext',
	author='Ion',
	author_email='uriel@ionmobility.asia',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
