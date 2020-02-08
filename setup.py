#!/usr/bin/env python

"""setup"""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
  readme = readme_file.read()

with open('HISTORY.rst') as history_file:
  history = history_file.read()

requirements = [
    'Click>=7.0',
    'gmpy2>=2.0.8',
    'mock>=3'
]

setup_requirements = []

test_requirements = []

setup(
    author="Steven K Terry",
    author_email='stkterry@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A collection of Pi generators.",
    entry_points={},
    install_requires=requirements,
    license="MIT license",
    long_description_content_type='text/x-rst',
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pigen',
    name='pigen',
    packages=find_packages(include=['pigen', 'pigen.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/stkterry/pigen',
    version='0.1.5',
    zip_safe=False,
    data_files=[]
)
