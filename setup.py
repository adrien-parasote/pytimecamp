#!/usr/bin/python
# coding: utf-8
import io
import re
from setuptools import setup


with io.open('./pytimecamp/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError('Unable to find version string.')

with io.open('README.md', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='pytimecamp',
    version=version,
    description='Python wrapper for Timecamp API.',
    long_description=long_description,
    author='Adrien Parasote',
    author_email='adrien@parasote.com',
    include_package_data=True,
    url='https://github.com/adrien-parasote/pytimecamp',
    packages=['pytimecamp', ],
    install_requires=[
        'requests>=2.12.4',
    ],
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Office/Business :: Financial :: Accounting',
    ]
)