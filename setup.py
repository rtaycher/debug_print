#!/usr/bin/env python

from setuptools import setup
import os
import os.path


__version___ = open(os.path.join(os.path.dirname(__file__),
                                      "debug_print/VERSION")).read().strip()


long_description = open(os.path.join(os.path.dirname(__file__), "README.md")).read()

setup(name='debug_print',
      version=__version___,
      description="A mini library for printf style debugging.",
      long_description=long_description,
      keywords='debug printf-debugging',
      author='Roman A. Taycher',
      author_email='rtaycher1987@gmail.com',
      url='http://crouchofthewildtiger.com/',
      license='MIT/X11 License',
      include_package_data=True,
      zip_safe=False,
      )
