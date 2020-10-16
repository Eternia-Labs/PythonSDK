#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='sc-optimus-ml-python-sdk',
      version='0.0.1',
      description='This package is for optimus_ml python SDK.',
      author='smmahe',
      author_email='mahendren@smartclean.sg',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
)