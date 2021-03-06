#!/usr/bin/env python
"""
flask-discoverer
-------------

Flask extension that enables autodiscovery and broadcast of API endpoints
"""
from setuptools import setup


setup(
    name='flask-watchman',
    version='0.0.1',
    url='http://github.com/jonnybazookatone/flask-watchman/',
    license='MIT',
    author='Jonathan Elliott',
    author_email='jonathan.elliott@cfa.harvard.edu',
    description='Flask API generic microservice end points',
    long_description=__doc__,
    py_modules=['flask_watchman'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'Flask-discoverer'
    ],
    test_suite='tests',
    tests_require = [
        'flask-testing',
        'flask-restful',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
