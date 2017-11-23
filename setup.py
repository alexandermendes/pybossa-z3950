# -*- coding: utf8 -*-
"""
pybossa-z3950
-------------

A PyBossa plugin for Z39.50 integration.
"""

import os
import json
from setuptools import setup

info = os.path.join(os.path.dirname(__file__), 'pybossa_z3950', 'info.json')
version = json.load(open(info))['version']


try:
    here = os.path.dirname(__file__)
    long_description = open(os.path.join(here, 'docs', 'readme.rst')).read()
except:
    long_description = ""


requirements = ["Flask-Z3950>=1.0.1"]


setup(
    name="pybossa-z3950",
    version=version,
    author="Alexander Mendes",
    author_email="alexanderhmendes@gmail.com",
    description="A PyBossa plugin that provides Z39.50 integration.",
    license="BSD",
    url="https://github.com/alexandermendes/pybossa-z3950",
    packages=['pybossa_z3950'],
    long_description=long_description,
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=requirements,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: Z39.50",
    ],
)
