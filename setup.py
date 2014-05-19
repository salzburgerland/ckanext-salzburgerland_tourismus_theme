from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(
    name='ckanext-salzburgerland_tourismus_theme',
    version=version,
    description="Salzburgerland Toursismus theme",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Salzburgerland Tourismus',
    author_email='info@salzburgerland.com',
    url='http://salzburgerland.com',
    license='APL 2.0',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.salzburgerland_tourismus_theme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        # myplugin=ckanext.salzburgerland_tourismus_theme.plugin:PluginClass
        salzburgerland_tourismus_theme=ckanext.salzburgerland_tourismus_theme.plugin:SalzburgerlandTourismusThemePlugin
    ''',
)
