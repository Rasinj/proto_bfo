#!/usr/bin/env python

from distutils.core import setup

setup(name='Example',
      version='1.0',
      description='Example',
      author='ON',
      author_email='olle@nordesjo.net',
      install_requires=['protobuf'],
      url='none',
      packages=['proto','proto.compiled','proto_composite'],
     )
