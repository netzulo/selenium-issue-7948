# -*- coding: utf-8 -*-
"""Package qacode module can be installed and configured from here"""


from setuptools import setup, find_packages


setup(
    name='maybeissue',
    version="0.0.0",
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'selenium==3.141.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.6',
    ],
)
