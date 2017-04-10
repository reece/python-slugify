#!/usr/bin/env python

# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re
import os
import sys
import codecs


name = 'python-slugify'
package = 'slugify'
description = 'A Python Slugify application that handles Unicode'
url = 'https://github.com/un33k/python-slugify'
author = 'Val Neekman'
author_email = 'info@neekware.com'
license = 'MIT'
install_requires = ['Unidecode>=0.04.16']
classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = codecs.open(os.path.join(package, '__init__.py'), encoding='utf-8').read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)


if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    args = {'version': get_version(package)}
    print("You probably want to also tag the version now:")
    print("  git tag -a %(version)s -m 'version %(version)s' && git push --tags" % args)
    sys.exit()


setup(
    name=name,
    version=get_version(package),
    url=url,
    license=license,
    description=description,
    author=author,
    author_email=author_email,
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=classifiers,
    entry_points={'console_scripts': ['slugify=slugify.slugify:main']},
)
