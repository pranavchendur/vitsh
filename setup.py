#!/usr/bin/env python

from setuptools import setup

setup(name='vitsh',
      version='0.0.1',
      description='VIT Shell',
      author='The OnePlus',
      author_email='',
      url='https://vit.ac.in',
      packages=['vitsh', 'vitsh.builtins'],
      entry_points="""
      [console_scripts]
      vitsh = vitsh.shell:main
      """,
      )
