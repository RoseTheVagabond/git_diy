#!/usr/bin/python3

from setuptools import setup

setup (name = 'ugit', version = '1.0', packages = ['ugit'],
        entry_points = {
            'console_scripts' : [
                'ugit = ugit.main:main'
            ]
        })