#!/usr/bin/env python

import versioneer
from setuptools import setup, find_packages

setup(
    name='json-spec3',
    version="1.0.0",
    maintainer="Flavio Curella",
    maintainer_email="flavio.curella@gmail.com",
    description='Implements JSON Schema, JSON Pointer and JSON Reference.',
    author='Xavier Barbosa',
    author_email='clint.northwood@gmail.com',
    license='BSD',
    url='https://github.com/fcurella/json-spec/',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    package_data={
        'jsonspec': [
            'misc/schemas/**/*.json'
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords=[
        'json',
        'utilitaries',
        'validation',
        'json-pointer',
        'json-reference',
        'json-schema'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: OpenStack',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=[
        'six',
    ],
    extras_require={
        'cli': ['termcolor'],
    },
    entry_points={
        'console_scripts': [
            'json = jsonspec.cli:main',
        ],
        'jsonspec.cli.commands': [
            'validate = jsonspec.cli:ValidateCommand',
            'extract = jsonspec.cli:ExtractCommand',
            'add = jsonspec.cli:AddCommand',
            'remove = jsonspec.cli:RemoveCommand',
            'replace = jsonspec.cli:ReplaceCommand',
            'move = jsonspec.cli:MoveCommand',
            'copy = jsonspec.cli:CopyCommand',
            'check = jsonspec.cli:CheckCommand',
        ],
        'jsonspec.reference.contributions': [
            'spec = jsonspec.reference.providers:SpecProvider',
        ],
        'jsonspec.validators.formats': [
            'email = jsonspec.validators.util:validate_email',
            'hostname = jsonspec.validators.util:validate_hostname',
            'ipv4 = jsonspec.validators.util:validate_ipv4',
            'ipv6 = jsonspec.validators.util:validate_ipv6',
            'regex = jsonspec.validators.util:validate_regex',
            'uri = jsonspec.validators.util:validate_uri',
            'css.color = jsonspec.validators.util:validate_css_color',
            'rfc3339.datetime = jsonspec.validators.util:validate_rfc3339_datetime',
            'utc.datetime = jsonspec.validators.util:validate_utc_datetime',
            'utc.date = jsonspec.validators.util:validate_utc_date',
            'utc.time = jsonspec.validators.util:validate_utc_time',
            'utc.millisec = jsonspec.validators.util:validate_utc_millisec',
        ]
    },
)
