# -*- coding: utf-8 -*-
#!/usr/bin/env python

from setuptools import setup

version = "1.1.0"
readme = open('README.md').read()

setup(
    name='ya-dancer',
    version=version,
    description='Get a response json reflecting the current status of the site.',
    long_description=readme,
    author='David Paule',
    author_email='jdpaule@twig-world.com',
    url='https://github.com/TwigWorld/ya-dancer',
    packages=[
        'ya_dancer',
    ],
    include_package_data=True,
    install_requires=[
    ],
    zip_safe=False,
    keywords='ya-dancer',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
)
