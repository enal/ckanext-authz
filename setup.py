# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-authz',
	version=version,
	description="CKAN-1.x authorization for CKAN-2.x",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Esra Ünal',
	author_email='esra.uenal@fokus.fraunhofer.de',
	url='',
	license='AGPL',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.authz'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
    [ckan.plugins]
    old_authz=ckanext.authz.plugin:Authz
    
    [paste.paster_command]
    authz=ckanext.authz.commands.authz:Authentication
	""",
)
