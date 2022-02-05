#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
from os import getenv

#with open("README.rst") as readme_file:
#    readme = readme_file.read()

#with open("HISTORY.rst") as history_file:
#    history = history_file.read()

requirements = []

setup_requirements = []

test_requirements = []

setup(
    author="Miguel Andres-Martinez",
    author_email="miguel.andres-martinez@awi.de",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="testing some github automation",
    install_requires=requirements,
    license="GNU General Public License v2",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="",
    version="0.0.1",
    zip_safe=False,
)
